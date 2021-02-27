#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include "cards.h"
#include <stdio.h>
#include <stdlib.h>

void assert_card_valid(card_t c) {  
  assert(c.value > 1 && c.value <= 14);  
  assert(c.suit >= SPADES && c.suit < NUM_SUITS);  
}

const char * ranking_to_string(hand_ranking_t r) {  
  switch(r){    
  case STRAIGHT_FLUSH: return "STRAIGHT_FLUSH";     
  case FOUR_OF_A_KIND: return "FOUR_OF_A_KIND";        
  case FULL_HOUSE: return "FULL_HOUSE";        
  case FLUSH: return "FLUSH";  
  case STRAIGHT: return "STRAIGHT";      
  case THREE_OF_A_KIND: return "THREE_OF_A_KIND";  
  case TWO_PAIR: return "TWO_PAIR";        
  case PAIR: return "PAIR";  
  case NOTHING: return "NOTHING";    
  }  
  return "";  
}

char value_letter(card_t c) {
  if (2 <= c.value && c.value < 10){    
    return '0' + c.value;    
  } else {    
    switch(c.value){      
    case 10: return '0';      
    case 11: return 'J';      
    case 12: return 'Q';      
    case 13: return 'K';      
    case 14: return 'A';      
    }    
  }  
  return 'x';    
}

char suit_letter(card_t c) {  
  switch(c.suit){    
  case SPADES: return 's';    
  case HEARTS: return 'h';    
  case DIAMONDS: return 'd';    
  case CLUBS: return 'c';    
  case NUM_SUITS: return 'x';    
  }  
  return 'x';
}

void print_card(card_t c) {  
  printf("%c%c", value_letter(c), suit_letter(c));  
}

card_t card_from_letters(char value_let, char suit_let) {
	
  card_t temp;
  
  if ('0' < value_let && value_let <= '9'){    
    temp.value = value_let - '0';    
  } else {    
    switch(value_let){      
    case '0': temp.value = 10; break;      
    case 'J': temp.value = 11; break;      
    case 'Q': temp.value = 12; break;      
    case 'K': temp.value = 13; break;      
    case 'A': temp.value = 14; break;      
    default: temp.value = 20;      
    }    
  }
  
  switch(suit_let){    
  case 's': temp.suit = SPADES; break;    
  case 'h': temp.suit = HEARTS; break;    
  case 'd': temp.suit = DIAMONDS; break;    
  case 'c': temp.suit = CLUBS; break;    
  default: temp.suit = 'x';    
  } 
  
  assert_card_valid(temp);  
  return temp;  
}

card_t card_from_num(unsigned c) { 
  
  card_t temp;  
  int c_suit = c / 13;  
  int c_val = c % 13;
  
  switch(c_suit){    
  case 0: temp.suit = SPADES; break;    
  case 1: temp.suit = HEARTS; break;    
  case 2: temp.suit = DIAMONDS; break;    
  case 3: temp.suit = CLUBS; break;    
  }
  
  if (c_val >= 2){    
    temp.value = c_val;    
  }  
  else {    
    temp.value = c_val + 13;    
  }  
  return temp;  
}
