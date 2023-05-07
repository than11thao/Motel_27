var eyeOpen = document.querySelector('.eye-open'),
    eyeClose = document.querySelector('.eye-close'),
    action_ps = document.querySelector('.action-password');
    eyeClose.onclick=function(){
        this.classList.remove('fa-eye-slash');
        eyeOpen.classList.add('fa-eye');
        action_ps.setAttribute("type","text")
    }
    eyeOpen.onclick=function(){
        this.classList.remove('fa-eye');
        eyeClose.classList.add('fa-eye-slash');
        action_ps.setAttribute("type","password");
    }