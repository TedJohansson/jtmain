$(window).scroll(function() {
  var scroll = $(window).scrollTop();
  if ( scroll > 200) {
      document.getElementById("header-img").src = document.getElementById("header-img").src.replace("header.", "header-small.")
      $("#header").css("position", "fixed")
      $("#header").css("padding-left", "calc(25% - 8px)")
      $("#header-img").css("width", "calc(50% - 1px)")
      $(".container").css("margin-top", "calc(100vw / 6.9)")
  }
  else if (scroll < 200){
      $("#header").css("position", "relative")
      $("#header").css("padding-left", "calc(25% - 3px)")
      $("#header-img").css("width", "calc(50% + 6px)")
      $(".container").css("margin-top", "0")
      document.getElementById("header-img").src = document.getElementById("header-img").src.replace("header-small.", "header.")
  }
  position = scroll;
});