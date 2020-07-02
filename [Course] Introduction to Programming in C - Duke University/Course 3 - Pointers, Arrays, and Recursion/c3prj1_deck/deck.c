#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "deck.h"
#include "time.h"

void print_hand(deck_t * hand){
  card_t ** card_p = hand->cards;  
  
  for (int i = 0; i < (hand->n_cards); i++) {    
    print_card(**card_p);    
    printf("%s", " ");    
    card_p++;    
  }  
}

int deck_contains(deck_t * d, card_t c) {
  card_t ** card_p = d->cards;
  
  for (int i = 0; i < (d->n_cards); i++) {    
    if (suit_letter(**card_p) == suit_letter(c) && value_letter(**card_p) == value_letter(c)) {      
      return 1;      
    }    
    card_p++;    
  }  
  return 0;     
}

void swap(card_t ** ptr1, card_t ** ptr2) {  
  card_t * temp_card = *ptr1;  
  *ptr1 = *ptr2;  
  *ptr2 = temp_card;  
}

void shuffle(deck_t * d){
  card_t ** card_p = d->cards;  
  int sz = (int)(d->n_cards);
  
  for (int i = 0; i < (d->n_cards); i++) {    
    int rand_index = ((int)rand()) % sz;    
    swap(card_p + i, card_p + rand_index);    
  }  
}

void assert_full_deck(deck_t * d) {

  card_t ** card_p = d->cards;  
  deck_t temp_deck;
  
  temp_deck.cards = d->cards;
  
  for (int i = 0; i < (d->n_cards); i++) {    
    card_t temp_card = **card_p;    
    assert_card_valid(temp_card);   
    
    if (i > 0) {      
      temp_deck.n_cards = (size_t)i;      
      assert(!deck_contains(&temp_deck, temp_card));      
    }    
    card_p++;    
  } 
}

void add_card_to(deck_t * deck, card_t c) {  
  deck->n_cards++;  
  deck->cards = realloc(deck->cards, (deck->n_cards) * sizeof(*(deck->cards)));  
  deck->cards[deck->n_cards - 1] = NULL;  
  deck->cards[deck->n_cards - 1] = realloc(deck->cards[deck->n_cards - 1], sizeof(*(deck->cards[deck->n_cards - 1])));  
  deck->cards[deck->n_cards - 1]->suit = c.suit;  
  deck->cards[deck->n_cards - 1]->value = c.value;
}

card_t * add_empty_card(deck_t * deck) { 
  card_t *temp_card = malloc(sizeof(*temp_card));  
  temp_card->suit = 0;  
  temp_card->value = 0;  
  deck->n_cards++;  
  deck->cards = realloc(deck->cards, (deck->n_cards) * sizeof(*(deck->cards)));  
  deck->cards[deck->n_cards - 1] = temp_card;  
  return temp_card;
}

deck_t * make_deck_exclude(deck_t * excluded_cards) {

  card_t temp_card;  
  deck_t *res_deck = malloc(sizeof(*res_deck));  
  res_deck->n_cards = 0;  
  res_deck->cards = NULL;  
  int c; 
  
  for (unsigned i = 0; i < 52; i++) {    
    temp_card = card_from_num(i);    
    c = deck_contains(excluded_cards, temp_card);
    
    if (c == 0) {      
      add_card_to(res_deck, temp_card);      
    }    
  }  
  return res_deck;
}

deck_t * build_remaining_deck(deck_t ** hands, size_t n_hands) {

  deck_t *temp_deck;  
  deck_t *d = malloc(sizeof(*d));  
  deck_t *res_deck;
  
  d->n_cards = 0;
  d->cards = NULL;  
  card_t *temp_card;
  
  for (size_t i = 0; i < n_hands; i++) {    
    temp_deck = hands[i];    
    for (size_t j = 0; j < temp_deck->n_cards; j++) {      
      temp_card = temp_deck->cards[j];      
      if (temp_card->value != 0) {	
		if (deck_contains(d, *temp_card) == 0) {	  
		  add_card_to(d, *temp_card);	  
		}	
      }      
    }    
  }
  
  res_deck = make_deck_exclude(d);  
  free_deck(d);
  
  return res_deck;
}

void free_deck(deck_t * deck) {
  for (size_t i = 0; i < deck->n_cards; i++) {    
    free(deck->cards[i]);    
  }
  
  free(deck->cards);  
  free(deck);
}
