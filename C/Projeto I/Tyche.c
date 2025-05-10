#include <stdio.h>
#include <string.h>
#include <locale.h>

int main (){
    setlocale(LC_ALL, "pt_BR.UTF-8");

    int i, j;
    char palavra[20];
    printf("Digite uma palavra para verificar se ela é um palindromo:");
    fgets(palavra, 20, stdin);
    palavra[strcspn(palavra, "\n")]= '\0';

    for (i = 0; palavra[i] != '\0'; i++){
        for (j = i+1; palavra[j] != '\0'; i++){
            if(palavra[i] == palavra[j]){
                printf("%c se repete\n", palavra[i]);
                break;
            }
        }
    }
return 0;
}