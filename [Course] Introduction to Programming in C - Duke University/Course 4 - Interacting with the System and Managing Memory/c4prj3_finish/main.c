#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <ctype.h>
#include "cards.h"
#include "deck.h"
#include "eval.h"
#include "future.h"
#include "input.h"

void score(deck_t **hands, size_t n_hands, int *win_arr) {  
  size_t index = 0;  
  int res = 0;  
  int tie = 0;  
  
  for (size_t j = 1; j < n_hands; j++) {    
    res = compare_hands(hands[index], hands[j]);
    
    if (res == -1) {      
      index = j;      
      tie = 0;      
    }
    
    if (res == 0) {      
      tie = 1;      
    }    
  }
  
  if (tie) {    
    win_arr[n_hands]++;    
  } else {    
    win_arr[index]++;    
  }  
}

void free_fc(future_cards_t * fc) {  
  for (size_t i = 0; i < fc->n_decks; i++) {    
    free((fc->decks[i]).cards);    
  }  
  
  free(fc->decks);  
  free(fc);  
}

void free_all(future_cards_t *fc, deck_t **hands, size_t n_hands, deck_t *rem_deck, int *win_arr) {  
  free_fc(fc);
  
  for (size_t i = 0; i < n_hands; i++) {    
    free_deck(hands[i]);    
  }
  
  free(hands);  
  free_deck(rem_deck);  
  free(win_arr);  
}

int main(int argc, char ** argv) {
	
  if ((argc == 1) || (argc > 3)) {    
    fprintf(stderr, "Wrong number of Arguments");    
    return EXIT_FAILURE;    
  }
    
  int trials;  
  deck_t **hands;  
  deck_t *rem_cards;  
  size_t n_hands = 0;  
  FILE *f = NULL;  
  int *arr = NULL; 

  future_cards_t *fc = (future_cards_t *)malloc(sizeof(*fc));  
  fc->decks = NULL;  
  fc->n_decks = 0;
    
  if (argc == 2) {    
    trials = 10000;    
  } else {    
    trials = strToInt(argv[2]);    
  }

  f = fopen(argv[1], "r");  
  hands = read_input(f, &n_hands, fc);  
  rem_cards = build_remaining_deck(hands, n_hands);  
  arr = (int *)realloc(arr, (n_hands + 1)*sizeof(*arr));  
  
  for (size_t k = 0; k < n_hands + 1; k++) {    
    arr[k] = 0;    
  }

  for (int i = 0; i < trials; i++) {    
    shuffle(rem_cards);    
    future_cards_from_deck(rem_cards, fc);    
    score(hands, n_hands, arr);    
  }
  
  for (size_t h = 0; h < n_hands; h++) {    
    printf("Hand %zu won %u / %u times (%.2f%%)\n", h, arr[h], trials, 100 * (float)arr[h] / (float)trials);    
  }
  
  printf("And there were %u ties\n", arr[n_hands]);  
  free_all(fc, hands, n_hands, rem_cards, arr);  
  fclose(f);
  
  return EXIT_SUCCESS;
}
