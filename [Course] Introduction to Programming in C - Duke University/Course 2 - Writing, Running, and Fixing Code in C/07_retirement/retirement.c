#include <stdio.h>
#include <stdlib.h>

struct _retire_info {  
  int months;  
  double contribution;  
  double rate_of_return;  
};
typedef struct _retire_info retire_info;

void retirement(int startAge, double initial, retire_info working, retire_info retired){
  int current_months = startAge;
  int current_age = current_months / 12;  
  int working_months = current_months + working.months; 
  double returns;
    
  while(current_months < working_months){    
    printf("Age %3d month %2d you have $%.2lf\n", current_age, current_months % 12, initial);    
    returns = initial * (working.rate_of_return / 100 / 12);    
    initial = initial + returns + working.contribution;    
    current_months++;    
    if(current_months % 12 == 0){      
      current_age++;      
    }    
  }
   
  int retired_months = current_months + retired.months;
    
  while(current_months < retired_months){    
    printf("Age %3d month %2d you have $%.2lf\n", current_age, current_months % 12, initial);    
    returns = initial * (retired.rate_of_return / 100 / 12);    
    initial = initial + returns + retired.contribution;    
    current_months++;    
    if(current_months % 12 == 0){      
      current_age++;      
    }    
  }  
}

int main(){  
  retire_info working;  
  working.months = 489;  
  working.rate_of_return = 4.5;  
  working.contribution = 1000;
  
  retire_info retired;  
  retired.months = 384;  
  retired.rate_of_return = 1;  
  retired.contribution = -4000;
  
  retirement(327, 21345, working, retired);
  
  return 0;
}
