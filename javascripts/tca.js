
var TCADB = {};
TCADB.parameters = {};
TCADB.parameters.location = "";
TCADB.parameters.username = sessionStorage.username;
TCADB.parameters.sessionid = sessionStorage.sessionid;
TCADB.parameters.user = {};

TCADB.newsfeed = {};

TCADB.URLs = {};
TCADB.URLs.request = "/clientrequest";	//with command
TCADB.URLs.secure_redirect_request = "/secure_redirect_request";
TCADB.URLs.getfile = "/resources2";		//server: from Blobstore

TCADB.threads = [];
TCADB.currentthreadid = 0;

TCADB.files = {};

TCADB.unique_number = 0;

var here = window.location.href;	//URL

console.log("location:" + here);
console.log("origin:" + window.location.origin);

TCADB.parameters.location = window.location.origin;

TCADB.system = {};

function execute(command){
  //	executes command or list of commands

  	if (command === undefined) return command;

  	var result;
  	if (command instanceof Array)
  	{
  		var l = command.length;
  		var result;
  		for (var c = 0; c < l; c++){

  			result = execute(command[c]);

  		};
  	}else{
  		result = command.function(command.parameters);
  	};
  	return result;
};

function newThread(parameters){
  //	start new execution thread
  //
  //	parameters.protected	when to be run as protected transaction

  	if (parameters === undefined){
  		protected = false;	//default
  	}else{

  		var protected = parameters.protected;

  		if(protected === undefined){
        protected = false;
      };

  	};

  	// new thread id (end of array):
  	var id = TCADB.threads.length;

  	TCADB.threads[id] = {};
  	TCADB.threads[id].id = id;
  	TCADB.threads[id].waitcount = 0;
  	TCADB.threads[id].protected = protected;
  	TCADB.threads[id].queue = [];			//commands
  	TCADB.threads[id].context = {};		//local properties

  	TCADB.currentthreadid = id;			//this

  	return TCADB.threads[id];
};

function addCommandToThread(parameters){
  //	add command(s) to thread queue
  //
  //	parameters.thread		object
  //	parameters.command	command or array of commands;
  //					array of commands: pushed one by one;

  	var thread = parameters.thread;
  	var command = parameters.command;

  	if (command instanceof Array){

  		var l = command.length;
  		for (var c = 0; c < l; c++)	thread.queue.push(command[c]);

  	}else{

  		thread.queue.push(command);

  	};
};

function setPropertyInThreadContext(parameters){
  //	set (temporary) property to be used in this thread
  //
  //	parameters.thread		object
  //	parameters.propname
  //	parameters.propvalue

  	parameters.thread.context[parameters.propname] = parameters.propvalue;
};

function getPropertyFromThreadContext(parameters){
  //	get (temporary) property from thread context
  //
  //	parameters.thread		object
  //	parameters.propname

  	return parameters.thread.context[parameters.propname];
};

function runThreads(){
  //
  //	thread execution will be interleaved, if not protected;
  //	there can be only 1 active protected thread, the only active then;

  	if (TCADB.threads.length === 0){
  //		requestAnimationFrame(runThreads);	//to stay active
  //not in use for now (all threads done; waiting for any user event)
  		return;
  	};
  	var id = TCADB.currentthreadid;

  	var command;
  	var thread = TCADB.threads[id];
  	var protected = thread.protected;
  	var threadcount;

  	if (protected){
  		//run protected thread exclusively:

  		threadcount = TCADB.threads.length;
  		//when unequal: the current thread was killed by a command (error cases)
  		while (threadcount === TCADB.threads.length &&(thread.waitcount === 0 && thread.queue.length > 0)){

  			//execute 1 queue entry (can be array):
  			command = thread.queue[0];	//first of queue
  			thread.queue.splice(0,1);	//delete from queue
  			thread.queue.length -= 1;
  			execute(command);			//can kill threads

  		};

      //Test if thread is killed
  		if (threadcount === TCADB.threads.length){
  			if (thread.queue.length === 0){
  				//thread ready, destroy it:
  				delete TCADB.threads[id];

  				//run other threads (if any):
  				//(process other events first)

  				TCADB.currentthreadid = 0;
  				threadcount = TCADB.threads.length;
  			};
  		}else{
  			TCADB.currentthreadid = 0;
  		};

  		//wait for event:
  		requestAnimationFrame(runThreads);
  		return;
  	};

  	//at this point there are active protected threads
  	//do non protected threads:

  	var waiting = 0;

  	threadcount = TCADB.threads.length;


    //ends when all threads are waiting (can be: none, when all ready)
    //protected threads are separated
  	while (waiting <  TCADB.threads.length && !protected){
  		thread = TCADB.threads[id];

  		//set thread as current:
  		TCADB.currentthreadid = id;

  		protected = thread.protected;

  		if (!protected && thread.waitcount === 0){
  			//execute 1 queue entry (can be array):
  			command = thread.queue[0];	//first of queue
  			thread.queue.splice(0,1);	//delete from queue
  			execute(command);			//can kill threads

        //test if thread is killed
  			if (threadcount === TCADB.threads.length){
  				if (thread.queue.length === 0){
  					//thread ready, destroy it:
  					TCADB.threads.splice(id,1);
  					id -= 1;	//count finished thread
  				};
  			}else{
  				id -= 1;	//count killed thread
  			};
  		}else{
  			//protected thread is counted, will be executed next
  			waiting += 1;
  		};
  		if (!protected){
  			//go to next thread:
  			id += 1;
  			if (id >= TCADB.threads.length) id = 0;
  			TCADB.currentthreadid = id;
  		};
  	};
  	//at this point there are only waiting threads or none:
  	if (waiting > 0) requestAnimationFrame(runThreads);
};

function killThread(thread){

  	//kill thread:
  	var id = thread.id;
  	TCADB.threads.splice(id,1);
  	TCADB.currentthreadid = 0;
};

function killAllThreads(){

  	TCADB.threads = [];
  	TCADB.currentthreadid = 0;
};


function HttpRequest(parameters){
  //send explicit HttpRequest to server
  //NOTE: response is not processed by browser;
  //	  response has to be handled explicitly by follow up in thread
  //
  //	parameters.thread		in which this is called
  //	parameters.request	server command, TCA format with function byname:
  //					{fname:<string>,parameters:{<parameters as named properties>}}
  //	parameters.response	property name in thread context
  //	parameters.body		optional: content

  	//check valid session:
  	if (TCADB.parameters.sessionid === "none"){
  		//session was killed earlier, so:
  		return;
  	};

  	var thread = parameters.thread;
  	var request = parameters.request;
  	var response = parameters.response;
  	var body = parameters.body;

  	if (body === undefined) body = null;

  	var url = TCADB.URLs.request;		//server defined

    //  var url = TCADB.URLs.public_request;
    //  Make if statement to check for which handler the request is meant and set the 'url' variable to the requested handler.
    //  if ( parameters.url === "login" ) { url = TCADB.URLs.login_request; } else if ( parameters.url === "secure_data" ) { url = TCADB.URLs.secure_data_request; }

    //translate command to JSON:
  	var requestJSON = JSON.stringify(request);

    //create XMLHttpRequest (class supplied by browser):
    var xhr = new XMLHttpRequest();

  	//set call back function:
  	xhr.onreadystatechange = function(){
  		var xhrresponse = "";
  		//response from server is always JSON encoded (starts with: "{");
  		//plain text below here is used in case of error

  		//check result:

  		if (xhr.readyState === xhr.DONE){
  			if (xhr.status === 200 || xhr.status === 0){
  				if (xhr.responseText){
  					xhrresponse = xhr.responseText;
  					//console.log(xhrresponse,xhr.status);

  					//server app checks session:
  					if (xhrresponse.substring(0,16) === "invalid session:"){
  						//kill session:
  						sessionStorage.sessionid = "none";
  						sessionStorage.login = "logged_out";
  						sessionStorage.username = "";

  						alert("Please login to use this service");

  						//kill all threads:
  						killAllThreads();

  						//back to main page:
  						window.location.href = window.location.origin;
  						return;
  					};
  				}else{
  					console.log("HttpRequest[" + url + "] no response text");
  					xhrresponse = "HttpRequest[" + url + "] no response text";
  				};
  			}else{
  				console.log("HttpRequest[" + url + "] status: " + xhr.status);
  				xhrresponse = "HttpRequest[" + url + "] status: " + xhr.status;
  			};

  			//save reponse text for processing next (in thread):
  			setPropertyInThreadContext({thread:thread,propname:response,propvalue:xhrresponse});

  			thread.waitcount -= 1;

  			//continue thread execution, if any:
  			runThreads();
  		};
  	};

  	thread.waitcount += 1;

  	xhr.open("POST",url,true);
  	xhr.setRequestHeader("command",requestJSON);
  	xhr.setRequestHeader("username",sessionStorage.username);
  	xhr.setRequestHeader("sessionid",sessionStorage.sessionid);
  	xhr.setRequestHeader("Content-Type","text/plain");
  	xhr.send(body);
};

function HttpRedirectRequest(parameters){
  //send explicit HttpRequest to server
  //NOTE: response is not processed by browser;
  //	  response has to be handled explicitly by follow up in thread
  //
  //	parameters.thread		in which this is called
  //	parameters.request	server command, TCA format with function byname:
  //					{fname:<string>,parameters:{<parameters as named properties>}}
  //	parameters.response	property name in thread context
  //	parameters.body		optional: content

  	//check valid session:
  	if (TCADB.parameters.sessionid === "none"){
  		//session was killed earlier, so:
  		return;
  	};

  	var redirect = parameters.requested_redirect;

  	var url = TCADB.URLs.secure_redirect_request;		//server defined
    //  var url = TCADB.URLs.public_request;
    //  Make if statement to check for which handler the request is meant and set the 'url' variable to the requested handler.
    //  if ( parameters.url === "login" ) { url = TCADB.URLs.login_request; } else if ( parameters.url === "secure_data" ) { url = TCADB.URLs.secure_data_request; }


    //create XMLHttpRequest (class supplied by browser):
    var xhr = new XMLHttpRequest();

  	xhr.open("POST",url,true);
  	xhr.setRequestHeader("username",TCADB.parameters.username);
  	xhr.setRequestHeader("sessionid",TCADB.parameters.sessionid);
  	xhr.setRequestHeader("Content-Type","text/plain");
  	xhr.setRequestHeader("requested_redirect", redirect);
  	xhr.send(null);
};

function HttpRequestUpload(parameters){

  	if (TCADB.parameters.sessionid === "none"){
  		//session was killed earlier, so:
  		return;
  	};

  	var thread = parameters.thread;
  	var url = parameters.url;
  	var response = parameters.response;
  	var file = parameters.file;


        //create XMLHttpRequest (class supplied by browser):
    var xhr = new XMLHttpRequest();

  	//set call back function:
  	xhr.onreadystatechange = function(){

  		var xhrresponse = "";
  		var haserror = true;

  		//check result:

  		if (xhr.readyState === xhr.DONE){
  			if (xhr.status === 200 || xhr.status === 0){
  				if (xhr.responseText){

  					xhrresponse = xhr.responseText;
  					//console.log("HttpRequestUpload[" + url + "]:" +  xhr.responseText);
  	        //console.log("HttpRequestUpload response:" + xhrresponse);
  				}else{
  					//console.log("HttpRequestUpload[" + url + "] no response text");
  					xhrresponse = "HttpRequest[" + url + "] no response text";
  				};
  			}else{
  				//console.log("HttpRequest[" + url + "] status: " + xhr.status);
  				xhrresponse = "HttpRequest[" + url + "] status: " + xhr.status;
  			};

  			setPropertyInThreadContext({thread:thread,propname:response,propvalue:xhrresponse});

  			thread.waitcount -= 1;

  			//continue thread execution, if any:
  			runThreads();
  		};
  	};

  	thread.waitcount += 1;

  	//headers are (over)written by browser! (from formdata)
  	xhr.open("PUT",url);
  	xhr.send(file);
    //console.log(file);
};

function httpSimple(parameters, callback){

  if (TCADB.parameters.sessionid === "none"){
  	return;
  };

  var request = parameters.request;
  var body = parameters.body;

  if (body === '') body = null;

  var url = TCADB.URLs.request;

  var requestJSON = JSON.stringify(request);

  var xhr = new XMLHttpRequest();

  xhr.onreadystatechange = function(){

  		var xhrresponse = "";

  		if (xhr.readyState === xhr.DONE){
  			if (xhr.status === 200 || xhr.status === 0){
  				if (xhr.responseText){

  					xhrresponse = xhr.responseText;
  					//console.log(xhrresponse,xhr.status);

  					if (xhrresponse.substring(0,16) === "invalid session:"){
  						sessionStorage.sessionid = "none";
  						sessionStorage.login = "logged_out";
  						sessionStorage.username = "";

  						alert("Please login to use this service");

  						window.location.href = window.location.origin;
  						return;
  					};
  				}else{
  					console.log("HttpRequest[" + url + "] no response text");
  					xhrresponse = "HttpRequest[" + url + "] no response text";
  				};
  			}else{
  				//console.log("HttpRequest[" + url + "] status: " + xhr.status);
  				xhrresponse = "HttpRequest[" + url + "] status: " + xhr.status;
  			};
        if(callback != undefined){
          callback(xhrresponse);
        };
  		};
  	};

  	xhr.open("POST",url,true);
  	xhr.setRequestHeader("command",requestJSON);
    xhr.setRequestHeader("routing",parameters.routing);
  	xhr.setRequestHeader("username",sessionStorage.username);
  	xhr.setRequestHeader("sessionid",sessionStorage.sessionid);
  	xhr.setRequestHeader("Content-Type","text/plain");
  	xhr.send(body);

};

function UserRequestSimple(parameters,callback){

  var content = parameters.content;

  if(parameters.routing === undefined){

    var routing = "main";

  }else{

    var routing = parameters.routing;

  };

	var request = {fname:parameters.server,parameters:{request:content}};

	if(parameters.body === undefined){
	    var body = '';
	}else{
		var body =  JSON.stringify(parameters.body);
	};

  var params = {};
  params.request = request;
  params.body = body;
  params.routing = routing;

	httpSimple(params, callback);

};


var TCAUTIL = {};
TCAUTIL.randomString = function(length){

  var N = length;

  var random = Array(N+1).join((Math.random().toString(36)+'00000000000000000').slice(2, 18)).slice(0, N);

  //var string = Math.random().toString(36).substring(length);

  return random;
};
TCAUTIL.jsonCheck = function(string){
  try{
    JSON.parse(string);
  } catch(e){
    return false;
  }
  return true;
}
TCAUTIL.contains = function(substring,string){
  if(string.indexOf(substring) == -1){
    return false;
  } else {
    return true;
  };
};
TCAUTIL.makeurl = function(template){
  var url = "/sp" + "?sessionid=" + sessionStorage.sessionid + "&username=" + sessionStorage.username + "&requested_page=" + template;
  return url;
};
TCAUTIL.add_select_option = function(list_id,input_id){

  var title = document.getElementById(input_id).value;
  var projects_list = document.getElementById(list_id);

  if(title != ""){

    var status = "correct";

    for(var i = 0; i < projects_list.length; i++) {
      if(title != projects_list.options[i].text){
        status = "correct";
      }else{
        status = "name_error"
      };
    };
    if(status == "name_error"){
      //message.innerHTML = "Project with the same name already exists."
      //message_div.style.display = "";
    }else if(status == "correct"){
      var option = document.createElement("option");
      option.text = title;
      projects_list.add(option);
    };
  }else{
    console.log('please set a project name.')
  };
};
TCAUTIL.isInArray = function(value, list){

  for(i=0; i<list.length; i++) {
      if(list[i]==value) {
          return true;
      };
  };
  return false;

};
TCAUTIL.fill_select = function(list,select){

  if(typeof select === 'string'){
    select = document.getElementById(select);
  };

  TCAUTIL.empty_select(select);

  for(var gss = 0; gss < list.length; gss ++){

    var option = document.createElement('option');

    option.text = list[gss];
    select.add(option);

  };

};
TCAUTIL.empty_select = function(selectbox){

    var i;

    for(i=selectbox.options.length-1;i>=0;i--){
      selectbox.remove(i);
    };

};
TCAUTIL.get_select_value = function(id){

  var elt = document.getElementById(id);

  if (elt.selectedIndex == -1)
      return null;

  return elt.options[elt.selectedIndex].text;
};
TCAUTIL.set_select_value = function(sel,val){

  var opts = sel.options;
  for(var opt, j = 0; opt = opts[j]; j++) {
    if(opt.value == val) {
        sel.selectedIndex = j;
        break;
    };
  };

};
TCAUTIL.array_remove = function(list,value){

    var i = TCAUTIL.array_index(list,value);

    if(i != -1) {
  	   list.splice(i, 1);
    };

    return list;
};
TCAUTIL.array_index = function(list,value){

  for(i=0; i<list.length; i++) {
      if(list[i]==value) {
          return i;
      };
  };

};
TCAUTIL.request = function(content,server,body,c_response,routing){

  UserRequestSimple({content:content,server:server,body:body,routing:routing},c_response);

};
TCAUTIL.response = function(response){

  var result = "";

  if(TCAUTIL.jsonCheck(response) == true){
    result = JSON.parse(response);
  }else{
    result = response;
  };

  return result;

};
TCAUTIL.navigate = function(parameters){

  console.log(parameters.url);
  var href = "/" + parameters.url;
  window.location.href = href;

};
TCAUTIL.checkemail = function(email){

  var testresults;
  var str = email;
  var filter=/^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;

  if(filter.test(str)){
      testresults=true;
  }else{
      testresults=false;
  };

  console.log("checkemail: " + testresults);
  return testresults;

};
TCAUTIL.profile_load = function(){

  json_s = localStorage.getItem('user');
  user = JSON.parse(json_s);
  TCADB.parameters.user = user;

};
TCAUTIL.sign_in = function(){

  function LoginResponse(response){

    //	thread step
    //	parameters.thread
    //	parameters.response	propname in threadcontext

    //var response = getPropertyFromThreadContext({thread:parameters.thread,propname:parameters.response});

    sessionStorage.login = "logged_in";
  	console.log(response);

  	var message = document.getElementById("login_message");
  	var div = document.getElementById("login_message_div");

  	if (response !== "successfully logged in"){

  		message.innerHTML = "Password or username is incorrect."
  		div.style.display = "block";

  		killAllThreads();
  		sessionStorage.login = "logged_out"

  	}else{

  		sessionStorage.login = "logged_in";
  		console.log(response);

      var param = {};
      param.url = 'dashboard';

      TCAUTIL.navigate(param);

  	};

  };

  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;

  // Make it so that every user navigates to the 'dashboard' regardless of admin status.

	if (username.length == 0 | password.length == 0 ){

	    alert("please fill in your username or password");

	}else{

	    sessionStorage.username = username;

	    //var nextcommand = {function:navigate,parameters:{URL:nav}};

	    //LoginRequest({username:username,password:password,nextcommands:nextcommand});

      var body = {};
      body.username = username;
      body.password = password;

      var response = LoginResponse;

      var content = '';
      var server = 'serverLogin';

      TCAUTIL.request(content,server,body,response);

	};

};
TCAUTIL.sign_out = function(){


  function LogoutResponse(response){

    	sessionStorage.login = "logged_out";
    	sessionStorage.username = "";

    	//killAllThreads();

    	window.location.href = window.location.origin;
  };

	/*var request = {fname:"serverLogout",parameters:{}};

	var thread = newThread();
	addCommandToThread({thread:thread,command:{function:HttpRequest,	 parameters:{thread:thread,
													  	 request:request,
														 response:"userresponse"}}});
	addCommandToThread({thread:thread,command:{function:LogoutResponse,parameters:{thread:thread,
														 response:"userresponse"}}});
	//Server 			deletes session server side
	//LogoutResponse (here) deletes session client side

	runThreads(); */

  var content = '';
  var server = 'serverLogout';
  var response = LogoutResponse;

  TCAUTIL.request(content,server,null,response);

}
TCAUTIL.newSession = function(){

    function receiveSessionResponse(response){

      sessionStorage.sessionid = response;

      TCADB.parameters.sessionid = sessionStorage.sessionid;

      console.log("session: " + sessionStorage.sessionid);

    };

    var content = '';
    var server = 'newSession';
    var response = receiveSessionResponse;
    TCAUTIL.request(content,server,null,response);

}
TCAUTIL.upload = function(parameters,callback,uploadProgress){

  if (TCADB.parameters.sessionid === "none"){
    return;
  };

  var url = parameters.url;
  var file = parameters.file;


  var xhr = new XMLHttpRequest();


  xhr.onreadystatechange = function(){

    var xhrresponse = "";
    var haserror = true;

    if (xhr.readyState === xhr.DONE){
      if (xhr.status === 200 || xhr.status === 0){
        if (xhr.responseText){

          xhrresponse = xhr.responseText;
          //console.log("HttpRequestUpload[" + url + "]:" +  xhr.responseText);
          //console.log("HttpRequestUpload response:" + xhrresponse);
        }else{
          //console.log("HttpRequestUpload[" + url + "] no response text");
          xhrresponse = "HttpRequest[" + url + "] no response text";
        };
      }else{
        //console.log("HttpRequest[" + url + "] status: " + xhr.status);
        xhrresponse = "HttpRequest[" + url + "] status: " + xhr.status;
      };
      if(callback != undefined){
        callback(xhrresponse);
      };
    };
  };

  if(uploadProgress != undefined){
    xhr.upload.onprogress = uploadProgress;
  };

  xhr.open("PUT",url);
  xhr.send(file);

}
TCAUTIL.load_progress = function(response){

  if(response.lengthComputable){
    var completion = response.loaded / response.total;
    var rounded = Math.round(completion * 10) / 10;
    var percent = rounded * 100;
    return percent;
  }else{
    console.log("unable to determine completion")
  };

  console.log(response);

};
TCAUTIL.download = function(get_url,callback,downloadProgress){

  console.log(get_url);

  if(TCADB.parameters.sessionid === "none"){
    return;
  };

  var xhr = new XMLHttpRequest();


  xhr.onreadystatechange = function(){
    var xhrresponse = "";
    var haserror = true;

    if (xhr.readyState === xhr.DONE){
      if (xhr.status === 200 || xhr.status === 0){
        if (xhr.responseText){

          xhrresponse = xhr.responseText;
          //console.log("HttpRequestUpload[" + url + "]:" +  xhr.responseText);
          //console.log("HttpRequestUpload response:" + xhrresponse);
        }else{
          //console.log("HttpRequestUpload[" + url + "] no response text");
          xhrresponse = "HttpRequest[" + get_url + "] no response text";
        };
      }else{
        //console.log("HttpRequest[" + url + "] status: " + xhr.status);
        xhrresponse = "HttpRequest[" + get_url + "] status: " + xhr.status;
      };
      if(callback != undefined){
        callback(xhrresponse);
      };
    };
  };

  if(uploadProgress != undefined){
    xhr.upload.onprogress = downloadProgress;
  };

  xhr.open("GET",get_url,true);
  xhr.send( null );

};
TCAUTIL.line_breaks = function(text){

  text = text.replace(/\r\n/g, '<br/>').replace(/[\r\n]/g, '<br/>');
  return text;

};
TCAUTIL.r_line_breaks = function(text){

  text = text.replace(/<br\s*[\/]?>/gi, "\n");
  return text;

};
TCAUTIL.urlify = function(text) {
  var urlRegex = (/(([a-z]+:\/\/)?(([a-z0-9\-]+\.)+([a-z]{2}|aero|arpa|biz|com|coop|edu|gov|info|int|jobs|mil|museum|name|nato|net|org|pro|travel|local|internal))(:[0-9]{1,5})?(\/[a-z0-9_\-\.~]+)*(\/([a-z0-9_\-\.]*)(\?[a-z0-9+_\-\.%=&amp;]*)?)?(#[a-zA-Z0-9!$&'()*+.=-_~:@/?]*)?)(\s+|$)/gi)

  return text.replace(urlRegex, function(url) {
      return '<a href="' + url + '">' + url + '</a>';
  })
  // or alternatively
  // return text.replace(urlRegex, '<a href="$1">$1</a>')
  //var text = "Find me at http://www.example.com and also at http://stackoverflow.com";
  //var html = urlify(text);
};


var TCACOM = {};
TCACOM.execute = function(command){
  //	executes command or list of commands

  	if (command === undefined) return command;

  	var result;
  	if (command instanceof Array)
  	{
  		var l = command.length;
  		var result;
  		for (var c = 0; c < l; c++){

  			result = execute(command[c]);

  		};
  	}else{
  		result = command.function(command.parameters);
  	};
  	return result;
};
TCACOM.newThread = function(parameters){
  //	start new execution thread
  //
  //	parameters.protected	when to be run as protected transaction

  	if (parameters === undefined){
  		protected = false;	//default
  	}else{

  		var protected = parameters.protected;

  		if(protected === undefined){
        protected = false;
      };

  	};

  	// new thread id (end of array):
  	var id = TCADB.threads.length;

  	TCADB.threads[id] = {};
  	TCADB.threads[id].id = id;
  	TCADB.threads[id].waitcount = 0;
  	TCADB.threads[id].protected = protected;
  	TCADB.threads[id].queue = [];			//commands
  	TCADB.threads[id].context = {};		//local properties

  	TCADB.currentthreadid = id;			//this

  	return TCADB.threads[id];
};
TCACOM.addCommandToThread = function(parameters){
  //	add command(s) to thread queue
  //
  //	parameters.thread		object
  //	parameters.command	command or array of commands;
  //					array of commands: pushed one by one;

  	var thread = parameters.thread;
  	var command = parameters.command;

  	if (command instanceof Array){

  		var l = command.length;
  		for (var c = 0; c < l; c++)	thread.queue.push(command[c]);

  	}else{

  		thread.queue.push(command);

  	};
};
TCACOM.setPropertyInThreadContext = function(parameters){
  //	set (temporary) property to be used in this thread
  //
  //	parameters.thread		object
  //	parameters.propname
  //	parameters.propvalue

  	parameters.thread.context[parameters.propname] = parameters.propvalue;
};
TCACOM.getPropertyFromThreadContext = function(parameters){
  //	get (temporary) property from thread context
  //
  //	parameters.thread		object
  //	parameters.propname

  	return parameters.thread.context[parameters.propname];
};
TCACOM.runThreads = function(){
  //
  //	thread execution will be interleaved, if not protected;
  //	there can be only 1 active protected thread, the only active then;

  	if (TCADB.threads.length === 0){
  //		requestAnimationFrame(runThreads);	//to stay active
  //not in use for now (all threads done; waiting for any user event)
  		return;
  	};
  	var id = TCADB.currentthreadid;

  	var command;
  	var thread = TCADB.threads[id];
  	var protected = thread.protected;
  	var threadcount;

  	if (protected){
  		//run protected thread exclusively:

  		threadcount = TCADB.threads.length;
  		//when unequal: the current thread was killed by a command (error cases)
  		while (threadcount === TCADB.threads.length &&(thread.waitcount === 0 && thread.queue.length > 0)){

  			//execute 1 queue entry (can be array):
  			command = thread.queue[0];	//first of queue
  			thread.queue.splice(0,1);	//delete from queue
  			thread.queue.length -= 1;
  			execute(command);			//can kill threads

  		};

      //Test if thread is killed
  		if (threadcount === TCADB.threads.length){
  			if (thread.queue.length === 0){
  				//thread ready, destroy it:
  				delete TCADB.threads[id];

  				//run other threads (if any):
  				//(process other events first)

  				TCADB.currentthreadid = 0;
  				threadcount = TCADB.threads.length;
  			};
  		}else{
  			TCADB.currentthreadid = 0;
  		};

  		//wait for event:
  		requestAnimationFrame(runThreads);
  		return;
  	};

  	//at this point there are active protected threads
  	//do non protected threads:

  	var waiting = 0;

  	threadcount = TCADB.threads.length;


    //ends when all threads are waiting (can be: none, when all ready)
    //protected threads are separated
  	while (waiting <  TCADB.threads.length && !protected){
  		thread = TCADB.threads[id];

  		//set thread as current:
  		TCADB.currentthreadid = id;

  		protected = thread.protected;

  		if (!protected && thread.waitcount === 0){
  			//execute 1 queue entry (can be array):
  			command = thread.queue[0];	//first of queue
  			thread.queue.splice(0,1);	//delete from queue
  			execute(command);			//can kill threads

        //test if thread is killed
  			if (threadcount === TCADB.threads.length){
  				if (thread.queue.length === 0){
  					//thread ready, destroy it:
  					TCADB.threads.splice(id,1);
  					id -= 1;	//count finished thread
  				};
  			}else{
  				id -= 1;	//count killed thread
  			};
  		}else{
  			//protected thread is counted, will be executed next
  			waiting += 1;
  		};
  		if (!protected){
  			//go to next thread:
  			id += 1;
  			if (id >= TCADB.threads.length) id = 0;
  			TCADB.currentthreadid = id;
  		};
  	};
  	//at this point there are only waiting threads or none:
  	if (waiting > 0) requestAnimationFrame(runThreads);
};
TCACOM.killThread = function(thread){

  	//kill thread:
  	var id = thread.id;
  	TCADB.threads.splice(id,1);
  	TCADB.currentthreadid = 0;
};
TCACOM.killAllThreads = function(){

  	TCADB.threads = [];
  	TCADB.currentthreadid = 0;
};

var TCAUI = {};
TCAUI.buttonIX = function(element){
  element.onmouseenter = function(){
    element.style.opacity = "0.98";
    element.style.cursor = "pointer";
    element.style.WebkitTransition = '-webkit-transform 0.1s';
    element.style.transition = 'transform 0.1s';
    element.style.WebkitTransform = "translateY(-2px)";
    element.style.msTransform = "translateY(-2px)";
    element.style.transform = "translateY(-2px)";
  };
  element.onmouseleave = function(){
    element.style.position = "";
    element.style.cursor = '';
    element.style.opacity = "1";
    element.style.WebkitTransform = "translateY(0px)";
    element.style.msTransform = "translateY(0px)";
    element.style.transform = "translateY(0px)";
  };
  return element
};
TCAUI.remove_IX = function(element){
  element.onmouseenter = '';
  element.onmouseleave = '';
  element.onfocus = '';
  element.onblur = '';
  element.style.cursor = 'auto';
};
TCAUI.elementDisplay = function(id,display){
  el = document.getElementById(id);
  el.style.display = display;
};
TCAUI.addProgressBar = function(parent,width){

  var div = document.createElement('DIV');
  div.className = "file_upload_box";
  div.style.width = width;

  var par = document.createElement('P');
  par.className = "file_group_meta";
  par.id = TCAUTIL.randomString(10);
  div.appendChild(par);

  var bardiv = document.createElement('DIV');
  bardiv.className = "progress_bar";
  div.appendChild(bardiv);

  var bar = document.createElement('DIV');
  bar.className = "progress_load";
  bar.style.width = "0%";
  bar.id = TCAUTIL.randomString(10);

  bardiv.appendChild(bar);
  parent.appendChild(div);

  var ids = {};
  ids.par = par.id;
  ids.bar = bar.id;

  return ids;
};
TCAUI.render_order = function(order,parent){

  console.log(order);

  var div = document.createElement('BUTTON');
  div.className = "order_option";
  div.style.width = "20%";
  div.href = "#";
  div.onclick = function(){
    if(this.selected == false){
      TCAUI.order_details(this.order,'show');
      this.selected = true;
    }else{
      TCAUI.order_details(this.order,'hide');
      this.selected = false;
    }
  }
  div.style.paddingTop = "10px";
  div.style.paddingBottom = "10px";
  div.style.opacity = "1";
  div.id = String(order.number);
  div.order = order;
  div.selected = false;
  TCAUI.buttonIX(div);
  var img = document.createElement('IMG');
  img.className = "option_image";
  img.src = "resources/images/fileicon.png";
  img.style.width = "40%";
  img.style.marginTop = "25px";
  img.style.marginBottom = "25px";
  div.appendChild(img);
  var par = document.createElement('P');
  par.className = "order_option_title";
  par.style.width = "98%";
  par.innerHTML = order.service + "<br>" + order.datetime_added.substring(0,10);
  div.appendChild(par);
  parent.appendChild(div);
}
TCAUI.order_details = function(order,display){
  var div = document.getElementById('order_details');
  div.innerHTML = "";

  var order_div = document.createElement('DIV');
  order_div.className = "form-divider";
  order_div.style.borderStyle = "solid";
  order_div.style.borderWidth = "1px";
  order_div.style.borderColor = "black";
  order_div.style.width = "70%";
  order_div.order = order;
  order_div.id = "details" + String(order.number);
  order_div.innerHTML = "ORDER<br><br>"
  div.appendChild(order_div);

  for(var gg in order){

    if(typeof order[gg] != "object"){
      order_div.innerHTML += gg + ":  " + order[gg] + "<br>";
    }else{
      if(gg = "price"){

        var price = order[gg];
        var price_div = document.createElement('DIV');
        price_div.className = "form-divider";
        price_div.style.borderStyle = "solid";
        price_div.style.borderWidth = "1px";
        price_div.style.borderColor = "black";
        price_div.style.width = "70%";
        price_div.innerHTML = "PRICE<br><br>";
        for(var gs in price){
          if(gs != 'shoot_time' && gs != 'total'){
            price_div.innerHTML += gs + ":  " + price[gs] + "<br>";
          };
        };
        price_div.innerHTML += "<br> Total:  " + price.total + "<br>";
      };
    };
  };

  var design_button = document.createElement('A');
  design_button.className = "button top-button port-button services-button";
  design_button.innerHTML = "Check design";
  design_button.href = "#";
  design_button.design = order.design.name;
  design_button.onclick = function(){
    check_design(this.design);
  };
  TCAUI.buttonIX(design_button);
  order_div.appendChild(price_div);
  order_div.appendChild(design_button);


  var button_div = document.createElement("DIV");
  order_div.appendChild(button_div);

  var button = document.createElement("A");
  button.className = "w-inline-block news_item_button";
  button.order = order;
  button.onclick = function(){

    TCAUI.order_details(this.parentNode.order,'hide');
    this.parentNode.selected = false;

  };
  button.href = "#";
  TCAUI.buttonIX(button);
  button_div.appendChild(button);
  var cross = document.createElement("IMG");
  cross.className = "cross_image";
  cross.src = "resources/images/cross.png";
  cross.width = "32";
  button.appendChild(cross);

};
TCAUI.create_select_button = function(design_object, parent){

  var button = document.createElement('BUTTON');
  button.className = "order_option";
  button.style.width = "20%";
  button.style.paddingTop = "10px"
  button.style.paddingBottom = "10px"
  button.href = "#";
  button.id = design_object.name;
  button.design = design_object;
  button.selected = false;
  button.onclick = function(){

    var message = document.getElementById('select_design_message');
    message.innerHTML = this.design.name;

    design = this.design.name;
    //console.log(design);

  };
  TCAUI.buttonIX(button);

  var img = document.createElement('IMG');
  img.className = "option_image";
  img.style.width = "40%";
  img.style.marginTop = "25px";
  img.style.marginBottom = "25px";
  img.src = "resources/images/fileicon.png";
  button.appendChild(img);


  var par = document.createElement('P');
  par.className = "order_option_title";
  par.style.width = "98%";
  par.innerHTML = design_object.name;
  button.appendChild(par);

  parent.appendChild(button);

};
TCAUI.create_item = function(data, parent, name, onclick){

  var button = document.createElement('BUTTON');
  button.className = "order_option";
  button.style.width = "20%";
  button.style.paddingTop = "10px"
  button.style.paddingBottom = "10px"
  button.href = "#";
  button.id = name;
  button.element_data = data;
  button.selected = false;
  button.onclick = onclick;
  TCAUI.buttonIX(button);
  var img = document.createElement('IMG');
  img.className = "option_image";
  img.style.width = "40%";
  img.style.marginTop = "25px";
  img.style.marginBottom = "25px";
  img.src = "resources/images/fileicon.png"
  button.appendChild(img);


  var par = document.createElement('P');
  par.className = "order_option_title";
  par.style.width = "98%";
  par.innerHTML = name;
  button.appendChild(par);
  parent.appendChild(button);

};
TCAUI.display_message = function(message,div_id,par_id){
  document.getElementById(div_id).style.display = "";
  document.getElementById(par_id).innerHTML = message;
};
TCAUI.menu_button = function(url,parent,name){

  n_button = document.createElement('A');
  n_button.className = "button top-button port-button services-button";
  n_button.href = TCAUTIL.makeurl(url);
  n_button.innerHTML = name;
  TCAUI.buttonIX(n_button);
  document.getElementById(parent).appendChild(n_button);

}
TCAUI.colors_flat = {};
TCAUI.colors_flat.red = '#fc4551';
TCAUI.colors_flat.blue = '#42aef1';
TCAUI.colors_flat.green = '#4cf196';
TCAUI.colors_flat.yellow = '#fcc726';
TCAUI.colors_flat.grey = 'rgb(150,150,150)';
TCAUI.list_button = function(parent,data,ui_function){

  var display_button = document.createElement("A");
  display_button.className = "w-inline-block news_item_button list_item_button";
  display_button.dataset = data;
  display_button.onclick = ui_function;
  display_button.href = "#";

  parent.appendChild(display_button);

  TCAUI.buttonIX(display_button);

  var display_icon = document.createElement("IMG");
  display_icon.className = "down_arrow";
  display_icon.src = "resources/images/down_arrow.png";
  display_icon.width = "30";

  display_button.appendChild(display_icon);

};
TCAUI.cross_button = function(parent,data,ui_function){

  var cross_button = document.createElement('A');
  cross_button.className = "w-inline-block news_item_button list_item_button";
  cross_button.href = "#";
  cross_button.dataset = data;
  cross_button.onclick = ui_function;

  TCAUI.buttonIX(cross_button);

  var cross_image = document.createElement('IMG');
  cross_image.className = 'down_arrow';
  cross_image.src = 'resources/images/cross.png';
  cross_image.width = '35px';

  cross_button.appendChild(cross_image);
  parent_appendChild(cross_button);

}
TCAUI.button_ix_load = function(){

  var btns = document.getElementsByTagName("A");

  for(var bsz in btns){
    var el = btns[bsz];
    TCAUI.buttonIX(el);
  };

  var aaz = document.getElementsByTagName('BUTTON');

  for(var bsz in aaz){
    var el = aaz[bsz];
    TCAUI.buttonIX(el);
  };

  var aaf = document.getElementsByTagName('LABEL');

  for(var bsz in aaf){
    var el = aaf[bsz];
    TCAUI.buttonIX(el);
  };

};
TCAUI.setProgressbar = function(id, percent){
  var bar = document.getElementById(id);
  percent = percent.toString() + "%";
  bar.style.width = percent;
};
TCAUI.input_IX = function(element){

  element.style.borderColor = 'rgba(0,0,0,0)';

  element.onfocus = function(){
    element.style.borderColor = 'rgba(0,0,0,1)';
  };

  element.onblur = function(){
    element.style.borderColor = 'rgba(0,0,0,0)';
  };

};
TCAUI.apply_autosize = function(){

  var txtareas = document.getElementsByTagName('textarea');

  for(var area in txtareas){
    autosize(area);
  };

};
TCAUI.autosize_update = function(){

  var evt = document.createEvent('Event');
  evt.initEvent('autosize:update', true, false);
  ta.dispatchEvent(evt);

};

TCAUI.apance = {};
TCAUI.apance.file_item = function(filemeta,delf,updatef){
  // delf is DELETE function
  // updatef is SELECT A NEW FILE FOR THIS ITEM function
  // Use the following metadata:
  var name = filemeta.name;
  var size = filemeta.size;
  var type = filemeta.type;

  /*<div class="w-clearfix apance-item_select">
  <img src="images/file_symbol.png" class="apance-item_select_thumbnail">
  <p class="apancepar label center">file name</p>
  <img src="images/cross_symbol.png" data-ix="hover-still" class="apance-item_icon">
  <img src="images/triangle_symbol.png" data-ix="hover-still" class="apance-item_icon">
  </div> */

  var dd = html.div('w-clearfix apance-item_select');
  dd.id = filemeta.name + "div"; // Use later to update or remove this div in case of file changes.
  var fimg = html.img('resources/images/file_symbol.png','apance-item_select_thumbnail');
  var pp = html.p('apancepar label center');
  pp.innerHTML = filemeta.name + "<br>" + filemeta.type + "<br>" + filemeta.size;
  pp.id = filemeta.name + "pp"; // Use to update filemeta display paragraph;
  var fximg = html.img('resources/images/cross_symbol.png','apance-item_icon');
  fximg.id = filemeta.name + "del";
  fximg.onclick = delf;
  TCAUI.buttonIX(fximg);

  var faimg = html.img('resources/images/triangle_symbol.png','apance-item_icon');
  faimg.id = filemeta.name + "update"; // Use later to update this file item div paragraph;
  faimg.onclick = updatef;
  TCAUI.buttonIX(faimg);
  dd.appendChild(fimg);
  dd.appendChild(pp);
  dd.appendChild(fximg);
  dd.appendChild(faimg);

  // Caller function can add it to the right parent element;
  return dd;
};

var html = {};
html.div = function(cssname){
  var div = document.createElement('DIV');
  div.id = TCAUTIL.randomString(10);
  if(cssname != undefined && cssname != ""){
    div.className = cssname;
  };
  return div;
};
html.p = function(cssname){

  var par = document.createElement('P');
  par.id = TCAUTIL.randomString(10);

  if(cssname != undefined && cssname != ''){
    par.className = cssname;
  };

  return par;
};
html.h = function(cssname){

  var hdr = document.createElement('H');
  hdr.id = TCAUTIL.randomString(10);

  if(cssname != undefined && cssname != ''){
    hdr.className = cssname;
  };

  return hdr
};
html._input = function(type,cssname){
  var inp = document.createElement('INPUT');
  if(type == ''){
    inp.type = 'text';
  }else{
    inp.type = type;
  };
  inp.id = TCAUTIL.randomString(10);
  if(cssname != undefined && cssname != ""){
    inp.className = cssname;
  };
  return inp;
};
html.button = function(cssname){

  var btn = document.createElement('A');

  if(cssname != undefined && cssname != ''){
    btn.className = cssname;
  };

  TCAUI.buttonIX(btn);
  btn.id = TCAUTIL.randomString(10);

  return btn;
};
html.textarea = function(auto,cssname){
  var txtr = document.createElement('textarea');
  if(auto == true){
    autosize(txtr);
  };
  if(cssname != undefined && cssname != ''){
    txtr.className = cssname;
  };
  txtr.id = TCAUTIL.randomString(10);
  return txtr;
};
html._select = function(cssname,options){

  var sl = document.createElement('select');
  sl.id = TCAUTIL.randomString(10);
  TCAUTIL.fill_select(options,sl);

  if(cssname != undefined && cssname != ''){
    sl.className = cssname;
  };

  return sl;

};
html.img = function(src,cssname){
  var img_n = document.createElement('img');
  img_n.src = src;
  if(cssname != undefined && cssname != ''){
    img_n.className = cssname;
  };
  return img_n;
};
html.br = function(){
  return document.createElement('br');
};
html.byId = function(id){
  return document.getElementById(id);
};
html.byCss = function(css){
  return document.getElementsByClassName(css);
};
html.byTag = function(tag){
  return document.getElementsByTagName(tag);
};
html.getVal = function(id){
  return document.getElementById(id).value;
};
html.set_this = function(id){
  var el = html.byId(id);
  el.value = el.value;
};

TCAUI.button_ix_load();
TCAUI.apply_autosize();
