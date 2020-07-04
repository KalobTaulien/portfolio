//Scroll Spy Replacement
import ScrollOut from "scroll-out";

//For splitting header animations
import Splitting from "splitting";

import $ from 'jquery';

$(document).ready(function () {
    $('main').fadeIn(300, function () {
    });

    ScrollOut({
        cssProps: {
            visibleY: true,
            viewportY: true
        },
        onShown(el, ctx, scrollingElement) {
            el.classList.add("animated");
        },

    });

    Splitting({target: ['.rich-text h3', '.splitting']});


    /****************************************************
     * Mobile Nav Toggle
     ****************************************************/

    $('.navbar-toggler').on('click', function () {

        var mobileNav = $('#mobile-nav');

        if (mobileNav.hasClass('open')) {
            mobileNav.fadeOut('fast').removeClass('open');
            $('body,html').css('overflow', 'initial');
        } else {
            mobileNav.fadeIn('fast');
            $('#mobile-nav').addClass('open');
            $('body,html').css('overflow', 'hidden');
        }
    });


    var newLocation;

    $('.nav-link').click(function () {
        event.preventDefault();
        newLocation = this.href;
        $('main').fadeOut(300, newpage);
    });

    function newpage() {
        window.location = newLocation;
    }
});

/****************************************************
 * Horizontal Gallery JS
 ****************************************************/

$(document).ready(function () {
    if (document.getElementById('horizontalGallery')) {
        // init
        var controller = new ScrollMagic.Controller();

        // define movement of panels
        var wipeAnimation = new TimelineMax()
            // animate to second panel
            .to("#horizontalGallerySlide", 0.5, {z: -150})    // move back in 3D space
            .to("#horizontalGallerySlide", 1, {x: "-33%"})    // move in to first panel
            .to("#horizontalGallerySlide", 0.5, {z: 0})        // move back to origin in 3D space
            // animate to third panel
            .to("#horizontalGallerySlide", 0.5, {z: -150, delay: 1})
            .to("#horizontalGallerySlide", 1, {x: "-66%"})
            .to("#horizontalGallerySlide", 0.5, {z: 0})

        // create scene to pin and link animation
        new ScrollMagic.Scene({
            triggerElement: "#horizontalGallery",
            triggerHook: "onLeave",
            duration: "400%"
        })
            .setPin("#horizontalGallery")
            .setTween(wipeAnimation)
            .addTo(controller);
    }
});