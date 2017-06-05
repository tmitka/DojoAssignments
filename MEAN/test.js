var glazedDonuts = [
  {
    frosting: 'glazed',
    type: 'old fashioned',
    age: '45',
    time: 'minutes'
  },
  {
    frosting: 'glazed',
    type: 'regular',
    age: '5',
    time: 'minutes'
  },
  {
    frosting: 'glazed',
    type: 'jelly filled',
    age: '1',
    time: 'seconds'
  }
];

var purchase;
//You
if((glazedDonuts[0].age < 25 && glazedDonuts[0].time == 'minutes') || glazedDonuts[0].time == 'seconds'){
  //shop owner
  purchase = glazedDonuts[0];
}
else {
  console.log('sorry it has been out a bit longer');
}