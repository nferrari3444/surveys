

let liEls = document.querySelectorAll("#cards-carousel");
console.log(liEls)
let index = 0;

function show(increase) {
    console.log(increase)
    console.log(liEls)
    console.log('liEls.length', liEls.length)
  index = index + increase;
  console.log('index',index)
  index = Math.min(Math.max(index,0), liEls.length-1);
  liEls[index].scrollIntoView({behavior: 'smooth'});
}