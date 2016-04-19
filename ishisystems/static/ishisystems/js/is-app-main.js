var site = {
	showHideCap: function(){
		if($(".more-link span").text()=="more"){
			$(".expanded-cap").show('slow');
			$(".more-link span").text("\xa0\xa0less\xa0");
			$(".more-link .fa").removeClass("fa-caret-down").addClass("fa-caret-up");
		} else {
			$(".expanded-cap").hide('slow');
			$(".more-link span").text("more");
			$(".more-link .fa").removeClass("fa-caret-up").addClass("fa-caret-down");
		}
	},
	displayUSText : function(){
		$("#usText").removeClass("hidden");
		$("#zurichText").addClass("hidden")
		$("#indiaText").addClass("hidden");
		$("#usIndicator").removeClass("hidden");
		$("#zurichIndicator").addClass("hidden")
		$("#indiaIndicator").addClass("hidden");
	},
	displayZurichText : function(){
		$("#zurichText").removeClass("hidden");
		$("#usText").addClass("hidden")
		$("#indiaText").addClass("hidden");
		$("#zurichIndicator").removeClass("hidden");
		$("#usIndicator").addClass("hidden")
		$("#indiaIndicator").addClass("hidden");
	},
	displayIndiaText : function(){
		$("#indiaText").removeClass("hidden");
		$("#zurichText").addClass("hidden");
		$("#usText").addClass("hidden");
		$("#indiaIndicator").removeClass("hidden");
		$("#zurichIndicator").addClass("hidden")
		$("#usIndicator").addClass("hidden");
	},
	displayMoreOrLessPeopleImages : function(mode){
		if(mode=="EXPAND"){
			$(".expanded-section").show('slow');
			$(".collapsed-section").hide('slow');
		} else {
			$(".expanded-section").hide('slow');
			$(".collapsed-section").show('slow');
		}
	},
	openPopup : function (url) {
			window.open(url, "_blank", "");
	},
	goToNextQuote: function () {
		$("#carousel-quotes").carousel("next");
    return false;
	},
	goToPreviousQuote: function () {
		$("#carousel-quotes").carousel("prev");
		return false;
	}, 
	
};
