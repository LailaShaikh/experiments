#include <stdio.h>
#include <stdlib.h>

struct Book
{
  char name[15];
  int price;
};

int main()
{
  struct Book book;
  struct Book* ptr;
  ptr = &book;

  //strcpy(book.name, "navaneethan");
  strcpy(ptr->name,"navaneethan");
  //ptr->name = "navaneethan";
  printf("ptr %s", ptr->name);

  //struct Book b[10];
  //struct Book* p;
  //p = &b;

  return 0;
}
