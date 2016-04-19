var timerIDUS = null
var timerIDZurich = null
var timerIDIndia = null
var timerRunningUS = false
var timerRunningZurich = false
var timerRunningIndia = false

function stopclock(){
    if(timerRunningUS)
        clearTimeout(timerIDUS)
	
	if(timerRunningZurich){
        clearTimeout(timerIDZurich)
	}
	if(timerRunningIndia)
        clearTimeout(timerIDIndia)
		
    timerRunningUS = false
    timerRunningZurich = false
    timerRunningIndia = false
}

function startclock(){
    stopclock()
    showtimeInUS()
    showtimeInZurich()
    showtimeInAhemdabad()
}

function showtimeInUS(){
    d = new Date();
    utc = d.getTime() + (d.getTimezoneOffset() * 60000);
    now = new Date(utc + (3600000*-5));

	var hours = now.getHours();
    var minutes = now.getMinutes()
    var seconds = now.getSeconds()
    var timeValue = "" + ((hours > 12) ? hours - 12 : hours)
    timeValue  += ((minutes < 10) ? ":0" : ":") + minutes
    var timeMeridien  = (hours >= 12) ? " PM" : " AM"
    $("#USTime").text(timeValue); 
    $("#USTimeMeridien").text(timeMeridien); 
    timerIDUS = setTimeout("showtimeInUS()",1000)
    timerRunningUS = true
}
function showtimeInZurich(){
    d = new Date();
    utc = d.getTime() + (d.getTimezoneOffset() * 60000);
    now = new Date(utc + (3600000*1));

	var hours = now.getHours();
    var minutes = now.getMinutes()
    var seconds = now.getSeconds()
    var timeValue = "" + ((hours > 12) ? hours - 12 : hours)
    timeValue  += ((minutes < 10) ? ":0" : ":") + minutes
    var timeMeridien  = (hours >= 12) ? " PM" : " AM"
	$("#ZurichTime").text(timeValue); 
	$("#ZurichTimeMeridien").text(timeMeridien); 
    timerIDZurich = setTimeout("showtimeInZurich()",1000)
    timerRunningZurich = true
}
function showtimeInAhemdabad(){
    d = new Date();
    utc = d.getTime() + (d.getTimezoneOffset() * 60000);
    now = new Date(utc + (3600000*5.5));
	var hours = now.getHours();
    var minutes = now.getMinutes()
    var seconds = now.getSeconds()
    var timeValue = "" + ((hours > 12) ? hours - 12 : hours)
    timeValue  += ((minutes < 10) ? ":0" : ":") + minutes
    var timeMeridien  = (hours >= 12) ? " PM" : " AM"
    $("#IndiaTime").text(timeValue); 	
    $("#IndiaTimeMeridien").text(timeMeridien); 	
    timerIDIndia = setTimeout("showtimeInAhemdabad()",1000)
    timerRunningIndia = true
}
function stdTimezoneOffset(date) {
	var jan = new Date(date.getFullYear(), 0, 1,0,0,0,date.getTime());
    var jul = new Date(date.getFullYear(), 6, 1,0,0,0,date.getTime());
    return Math.max(jan.getTimezoneOffset(), jul.getTimezoneOffset());
}
function dst(offset) {
	var date = new Date();
    var utc = date.getTime() + (date.getTimezoneOffset() * 60000); // get UTC time in milliseconds
    var nd = new Date(utc + (3600000 * offset)); // Create net Date() for city with offset
    return date.getTimezoneOffset() < stdTimezoneOffset(date);
}
startclock();