$(document).ready(function() {
	$("#contactAddressUS").hide();
    $("#contactAddressZurich").hide();
    $("#contactAddressIndia").hide();
    $(".timeUS").show();
    $(".timeZurich").show();
    $(".timeIndia").show();

	$('.contactInformationUS').mouseenter(function() {
        $("#contactAddressUS").slideToggle(200);
		$(".timeUS").toggle();
    });
	$('.contactInformationUS').mouseleave(function() {
        $("#contactAddressUS").toggle();
		$(".timeUS").slideToggle(200);
    });
	
	$('.contactInformationZurich').mouseenter(function() {
        $("#contactAddressZurich").slideToggle(200);
		$(".timeZurich").toggle();
    });
	$('.contactInformationZurich').mouseleave(function() {
        $("#contactAddressZurich").toggle();
		$(".timeZurich").slideToggle();
    });
	
	$('.contactInformationIndia').mouseenter(function() {
        $("#contactAddressIndia").slideToggle(200);
		$(".timeIndia").toggle();
    });
	$('.contactInformationIndia').mouseleave(function() {
        $("#contactAddressIndia").toggle();
		$(".timeIndia").slideToggle();
    });
	$(".capabilities-block .main-section").hover(function() {
		$(this).find(".details").toggleClass("hidden");
	});
	$(".performance-table .main-section").hover(function() {
		$(this).find(".details").toggleClass("hidden");
		$(this).find(".heading").toggleClass("hidden");
	});  
	// Checks if attribute is supported by a browser
	function attributeSupported(attribute) {
	  return (attribute in document.createElement("input"));
	}
	//for browser that does not support html5 form validation:IE6-9,Safari etcs
	if (!attributeSupported("required") || ($.browser.safari)) { 
		$("#id_ques_form").validate();
		$("#id_contact_form").validate(); 
	}
	$('input, textarea').placeholder(); 
	 
	function applyActiveClass() { 
		 var con1 = $("ul.nav.navbar-nav.sub-menu li").hasClass("active");
		 var parentClass='';
		 var pattern = /dummyClass/;
		 if(con1) {
			  var classess =  $("ul.nav.navbar-nav.sub-menu li a").attr('class').split(" ");
			  //alert(classess);
			  for (var i = 0; i < classess.length; i++) { 
				    if (pattern.test(classess[i])) {
				    	parentClass = classess[i];
				    	//alert(parentClass);
				        break; 
				    }
				}; 
				if(parentClass !='')
					$("."+parentClass).addClass("active"); 
			   
		 } 
	}
	applyActiveClass();
	
	
	
		
		 
	 
	 
	
	 
	

});