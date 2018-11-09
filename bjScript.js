// Code goes here
///console.log("hello world!");

var suits = ["Hearts","Clubs","Spades","Diamonds"];
var values = ["Ace","King","Queen","Jack","Ten","Nine","Eight","Seven","Six","Five","Four","Three","Two"];
var deck=[];
var dealerCards, playerCards = [];

//elements on page
var dealerText = document.getElementById("Dealer");
var playerText = document.getElementById("Player");
var comments = document.getElementById("comments");
var dealButton = document.getElementById("btnDeal");
var twistButton = document.getElementById("btnTwist");
var stickButton = document.getElementById("btnStick");


twistButton.style.display = "none";
stickButton.style.display = "none";

function shuffleDeck()
{ 
  deck = [];
  for(var i=0;i<suits.length;i++)
  {
    for(var j=0;j<values.length;j++)
    {
      var card = {
        suit: suits[i],
        value: values[j],
        score: cardScore(values[j])
        }

      deck.push(card);
    }  
  }
  return deck;
}

function getNextCard()
{
  var randIndex = Math.trunc(Math.random()*deck.length);
  var randCard = deck[randIndex];
  deck.splice(randIndex,1);
  return randCard;
}
 

function runDeal()
{ 
  dealerText.innerText = "";
  playerText.innerText = "";
  
  var deck = shuffleDeck();
  console.log(deck);
  dealerCards = [getNextCard(),getNextCard()];
  console.log(dealerCards);
  for(var i=0;i<dealerCards.length;i++)
  {
      dealerText.innerText += getCardString(dealerCards[i]) + '\n';
  }
  dealerText.innerText += totalScore(dealerCards) + '\n'
  playerCards = [getNextCard(),getNextCard()]; 
  console.log(playerCards);
  for(var i=0;i<playerCards.length;i++)
  {
      playerText.innerText += getCardString(playerCards[i]) + '\n';
  }
  playerText.innerText += totalScore(playerCards) + '\n'
  twistButton.style.display = "inline";
  stickButton.style.display = "inline";
  comments.innerText = "Cards dealt";
  
}

function getCardString(myCard)
{
  return myCard.value + " of " + myCard.suit;
}

 
function runTwist()
{
    playerCards.push(getNextCard());
    console.log(playerCards);
    var pScore = totalScore(playerCards);
    playerText.innerText = "";
    for(var i=0;i<playerCards.length;i++)
    {
      playerText.innerText += getCardString(playerCards[i]) + '\n';
    }
    playerText.innerText += totalScore(playerCards) + '\n'

    if(pScore>21)
    {
      comments.innerText = "You're BUST";
      twistButton.style.display = "none";
      stickButton.style.display = "none";
    }
    else
    comments.innerText = "Want another?";
}

function rollDealer()
{
    var dScore = totalScore(dealerCards);
    while(dScore<17 || dScore < totalScore(playerCards))
    {
      dealerCards.push(getNextCard());
      dScore = totalScore(dealerCards);
    }
    console.log(dealerCards);
    dealerText.innerText = "";
    for(var i=0;i<dealerCards.length;i++)
    {
        dealerText.innerText += getCardString(dealerCards[i]) + '\n';
    }
    dealerText.innerText += totalScore(dealerCards) + '\n'
    if(dScore>21)
      comments.innerText = "Dealer bust";
}

function runStick()
{
    twistButton.style.display = "none";
    stickButton.style.display = "none";
    comments.innerText = "no more";
    rollDealer();
    checkWinner();
}

function cardScore(cardVal)
{
  switch(cardVal)
  {
    case 'Ace' : return 1;
    case 'Ten' : return 10;
    case 'Nine' : return 9;
    case 'Eight' : return 8;
    case 'Seven' : return 7;
    case 'Six' : return 6;
    case 'Five' : return 5;
    case 'Four' : return 4;
    case 'Three' : return 3;
    case 'Two' : return 2;
    default : return 10;
  }
}

function totalScore(cardsDealt)
{
   var score = 0;
   for(var i=0;i<cardsDealt.length;i++)
   {
        score += cardsDealt[i].score;
   }
   return score;
}

function checkWinner()
{
  var dealerScore = 0;
  var playerScore = 0;
  
  dealerScore = totalScore(dealerCards);
  playerScore = totalScore(playerCards);
  if(playerScore > 21)
    comments.innerText = "Player bust";
  else if(dealerScore > 21)
    comments.innerText = "Player Wins";
  else if(playerScore === 21 || playerScore > dealerScore)
    comments.innerText = "Player Wins";
  else
    comments.innerText = "Dealer Wins";
}
