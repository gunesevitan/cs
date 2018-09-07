#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include "cards.h"


#include <stdio.h>

#include <stdlib.h>



void assert_card_valid(card_t c) {
  
  assert(c.value >1 && c.value <=14);
  
  assert(c.suit >= SPADES && c.suit < NUM_SUITS);
  
}



const char * ranking_to_string(hand_ranking_t r) {
  
  switch(r){
    
  case STRAIGHT_FLUSH:
    
    return "STRAIGHT_FLUSH";
    

    
  case FOUR_OF_A_KIND:
    
    return "FOUR_OF_A_KIND";
    

    
  case FULL_HOUSE:
    
    return "FULL_HOUSE";
    

    
  case FLUSH:
    
    return "FLUSH";
    

    
  case STRAIGHT:
    
    return "STRAIGHT";
    

    
  case THREE_OF_A_KIND:
    
    return "THREE_OF_A_KIND";
    

    
  case TWO_PAIR:
    
    return "TWO_PAIR";
    

    
  case PAIR:
    
    return "PAIR";
    

    
  case NOTHING:
    
    return "NOTHING";
    
  }
  
  return "";
  
}



char value_letter(card_t c) {
  
  if(c.value > 1 && c.value < 10){
    
    return (c.value + '0');
    
  }
  

  
  switch(c.value){
    
  case VALUE_ACE:
    
    return 'A';
    

    
  case VALUE_KING:
    
    return 'K';
    

    
  case VALUE_QUEEN:
    
    return 'Q';
    

    
  case VALUE_JACK:
    
    return 'J';
    

    
  case 10:
    
    return '0';
    

    
  default:
    
    return 'x';
    
  }
  
}



char suit_letter(card_t c) {
  
  switch(c.suit){
    
  case SPADES:
    
    return 's';
    

    
  case HEARTS:
    
    return 'h';
    

    
  case DIAMONDS:
    
    return 'd';
    

    
  case CLUBS:
    
    return 'c';
    

    
  default:
    
    return 'x';
    
  }
  
}



void print_card(card_t c) {
  
  printf("%c%c", value_letter(c), suit_letter(c));
  
}



card_t card_from_letters(char value_let, char suit_let) {
  
  card_t temp;
  

  
  assert((value_let >= '2' && value_let <= '9') || value_let == 'A' || value_let == 'K'
	 
	 || value_let == 'Q' || value_let == 'J' || value_let == '0');
  
  assert( suit_let == 's' || suit_let == 'h' || suit_let == 'd' || suit_let == 'c' );
  

  
  if( value_let >= '2' && value_let <= '9' )
    
    temp.value = value_let - '0';
  

  
  switch(value_let){
    
  case 'A':
    
    temp.value = VALUE_ACE;
    
    break;
    

    
  case 'K':
    
    temp.value = VALUE_KING;
    
    break;
    

    
  case 'Q':
    
    temp.value = VALUE_QUEEN;
    
    break;
    

    
  case 'J':
    
    temp.value = VALUE_JACK;
    
    break;
    

    
  case '0':
    
    temp.value = 10;
    
    break;
    
  }
  

  
  switch(suit_let){
    

    
  case 's':
    
    temp.suit = SPADES;
    
    break;
    

    
  case 'h':
    
    temp.suit = HEARTS;
    
    break;
    

    
  case 'd':
    
    temp.suit = DIAMONDS;
    
    break;
    

    
  case 'c':
    
    temp.suit = CLUBS;
    
    break;
    
  }
  
  return temp;
  
}







card_t card_from_num(unsigned c) {
  

  
  card_t temp;
  
  assert( c < 52 );
  

  
  temp.value = c % 13 +2;
  
  temp.suit = c % 4;
  

  
  return temp;
  
}
