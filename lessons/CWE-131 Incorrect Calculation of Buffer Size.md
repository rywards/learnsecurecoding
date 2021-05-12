## What is an Incorrect Calculation of Buffer Size?

When creating buffers, it is imperative to ensure that you are allocating enough space to contain not only the data that you want to be held, but also a NULL pointer in order to know when the end of the buffer has been reached. In the event that there is not enough memory allocated for the data and the NULL pointer to be held in the buffer, a buffer overflow will occur. This can be dangerous because buffer overflows can crash applications and in some cases corrupt memory. This also applies to the creation of arrays, although they are not exactly the same as buffers. 

## Why is it important?

Buffer overflows are usually only a concern if you are coding in the languages C or C++, since most other languages handle memory allocation automatically. It still useful to know this concept when developing in higher-level languages, because it provides insight on what is going on behind the scenes. 

When developing your code, make sure the logic behind the allocation of buffer size takes into account any variability in buffer memory allocation and that it is taking into account the memory that needs to be reserved for the NULL pointer at the end of every buffer. 

**Example**

Below is an example of a buffer size miscalcuation: 
```c 

int i; 

unsigned int numWidgets; 

Widget **WidgetList; 

numWidgets = GetUntrustedSizeValue(); 

if ((numWidgets == 0) || (numWidgets > MAX_NUM_WIDGETS)) { 
  ExitError("Incorrect number of widgets requested!"); 
} 

WidgetList = (Widget **)malloc(numWidgets * sizeof(Widget *)); 

printf("WidgetList ptr=%p\n", WidgetList); 

for(i=0; i<numWidgets; i++) { 
  WidgetList[i] = InitializeWidget(); 
} 

WidgetList[numWidgets] = NULL; 

showWidgets(WidgetList); 

``` 

WidgetList is allocated memory based off of the number of widgets and size of the widget, and at first glance appears to be allocating enough memory to hold all of the widgets. A closer look, however, shows that it fails to take into account the memory needed to store a NULL pointer. As a result, the buffer is smaller than it needs to be, and this will result in buffer overflow. 

For more examples of this weakness and further information visit: <https://cwe.mitre.org/data/definitions/131.html>
