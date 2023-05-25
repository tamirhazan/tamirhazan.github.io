$(document).ready(function() {
	// Header Scroll
	$(window).on('scroll', function() {
		var scroll = $(window).scrollTop();

		if (scroll >= 50) {
			$('#header').addClass('fixed');
		} else {
			$('#header').removeClass('fixed');
		}
	});

	
	// Page Scroll
	var sections = $('section')
		nav = $('nav[role="navigation"]');

	$(window).on('scroll', function () {
	  	var cur_pos = $(this).scrollTop();
	  	sections.each(function() {
	    	var top = $(this).offset().top - 76
	        	bottom = top + $(this).outerHeight();
	    	if (cur_pos >= top && cur_pos <= bottom) {
	      		nav.find('a').removeClass('active');
	      		nav.find('a[href="#'+$(this).attr('id')+'"]').addClass('active');
	    	}
	  	});
	});
	nav.find('a').on('click', function () {
	  	var $el = $(this)
	    	id = $el.attr('href');
		$('html, body').animate({
			scrollTop: $(id).offset().top - 75
		}, 500);
	  return false;
	});

	// Mobile Navigation
	$('.nav-toggle').on('click', function() {
		$(this).toggleClass('close-nav');
		nav.toggleClass('open');
		return false;
	});	
	nav.find('a').on('click', function() {
		$('.nav-toggle').toggleClass('close-nav');
		nav.toggleClass('open');
	});
});


function formatBibtex(bibtex) {
    let splitEntry = bibtex.split(",");  // Split on commas
    splitEntry = splitEntry.map((item, index) => index === 0 ? item : "\n    " + item.trim());
    let formattedEntry = splitEntry.join(",");
    return formattedEntry;
}

var bibtexLinks = document.querySelectorAll('.bibtex-link');
var bibtexContents = document.querySelectorAll('.bibtex-content');
var copyLinks = document.querySelectorAll('.copy-btn');

bibtexContents.forEach(function(content, index) {
    var bibtex = content.textContent.trim();
    content.textContent = formatBibtex(bibtex);
});

bibtexLinks.forEach(function(link, index) {
  link.onclick = function(event) {
    event.preventDefault();
    bibtexContents.forEach(function(content, i) {
        if (i !== index) content.style.display = 'none';
    });
    if (bibtexContents[index].style.display === "none") {
        bibtexContents[index].style.display = "block";
    } else {
        bibtexContents[index].style.display = "none";
    }
  }
});

copyLinks.forEach(function(link, index) {
  link.addEventListener('click', function(event) {
    event.preventDefault();
    event.stopPropagation();

    var tempTextArea = document.createElement("textarea");
    document.body.appendChild(tempTextArea);
    tempTextArea.value = bibtexContents[index].textContent.trim();
    tempTextArea.select();
    document.execCommand("copy");
    document.body.removeChild(tempTextArea);
    alert("Copied the BibTeX to clipboard!");
  });
});
