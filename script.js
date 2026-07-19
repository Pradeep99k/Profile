const wrapper = document.querySelector('.wrapper');
const logolink = document.querySelector('.loginlink');
const registerlink = document.querySelector('.registerlink');
const btnpopup= document.querySelector('.btnLogin-popup');
const btniconclose= document.querySelector('.icon-close');

registerLink.addEventListener ( 'click, ()=>'{
    wrapper.classList.add('active');

});

loginLink.addEventListener ( 'click, ()=>'{
    wrapper.classList.remove('active');
    
});

btnpopup.addEventListener ( 'click, ()=>'{
    wrapper.classList.add('active-popup');
});

iconclose.addEventListener ( 'click, ()=>'{
    wrapper.classList.remove('active-popup');
});