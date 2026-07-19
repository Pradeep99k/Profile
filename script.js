const wrapper = document.querySelector('.wrapper');
const logoLink =document.querySelector('.login-link');
const registerLink =document.querySelector('.register-link');
const btnpopup= document.querySelector('.btnlogin-popup');
const btniconclose= document.querySelector('.icon-Close');

registerLink.addEventListener('click', () => {
    wrapper.classList.add('active');

});

loginLink.addEventListener ( 'click, ()=>'{
    wrapper.classList.remove('active');
    
});

btnpopup.addEventListener ( 'click, ()=>'{
    wrapper.classList.add('active-popup');
});

iconClose.addEventListener ( 'click, ()=>'{
    wrapper.classList.remove('active-popup');
});
