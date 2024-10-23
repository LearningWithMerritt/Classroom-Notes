# `Cascading Style Sheets`

<br>

___

<br>

Covered in this file:
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()



<br>

[`Back To Top`](#cascading-style-sheets)
___

<br>


# `CSS Defined`

`CSS (Cascading Style Sheets)` is a style sheet language used for describing the 
presentation of a document written in HTML or XML. 
* It defines how elements are displayed on a web page, including their layout, colors, fonts, and other visual aspects. 
* CSS allows developers to separate the structure and content of a webpage from its presentation, providing flexibility and maintainability.


A `stylesheet` is a collection of rules that defines the appearance of HTML elements. 
Can be external (linked file), internal (within HTML file), or inline (directly in an HTML tag).


<br>

[`Back To Top`](#cascading-style-sheets)
___

<br>

# `Comments`

<br>
```css
/* 
   CSS (Cascading Style Sheets) is a style sheet language used for describing the 
   presentation of a document written in HTML or XML. It defines how elements are 
   displayed on a web page, including their layout, colors, fonts, and other visual 
   aspects. CSS allows developers to separate the structure and content of a webpage 
   from its presentation, providing flexibility and maintainability.
*/

/* This is a basic CSS file with comments explaining each part. */

/*

Style Sheet: 
  A collection of rules that define the appearance of HTML elements. 
  Can be external (linked file), internal (within HTML file), or inline (directly in an HTML tag).

Selector:
   a pattern used to select and style HTML elements. 
   Selectors can target elements, classes, IDs, attributes, or combinations of these.

Class: 
  A way to apply styles to multiple elements. Defined with a period (.) in CSS and used in HTML with the class attribute.
  example: .classname

Pseudo-class: 
  a keyword added to a selector to style a specific state or condition of an element.
  example: element:pseudo-class

ID: 
  Similar to a class but should be unique on a page. Defined with a hash (#) in CSS and used in HTML with the id attribute.
  example: #id

Property:
   an attribute of an element that you want to style. 
   Examples include color, font-size, margin, and background-color.

Value:
   the specific setting assigned to a CSS property. 
   For example, #333 is a value for the color property.

Declaration:
   a combination of a CSS property and its corresponding value. 
   Declarations are enclosed in curly braces {}.
   example: property:value;

Rule:
   consists of one or more declarations, associated with a selector. 
   It defines how the selected elements should be styled.

Declaration Block:
   A declaration block is a group of one or more declarations within curly braces {}. 
   It is part of a CSS rule.

Rule------------------------------------|
selector {                              |      
   Declaration Block---------------|    |
   property:value;  Declaration    |    |
   property:value;  Declaration    |    |
   property:value;  Declaration    |    |
   property:value;  Declaration    |    |
   --------------------------------|    |
}                                       |  
----------------------------------------|


CSS Box Model: 
  Describes the layout of elements as a box with content, padding, border, and margin.

  +---------------------------------------------+
  |                  Margin-top                 |
  |  +---------------------------------------+  |
  |  |               Border-top              |  |
  |  |  +---------------------------------+  |  |
  |  |  |            Padding-top          |  |  |
  |  |  |  +-------------------------+    |  |  |
  |  |  |  |          Content        |    |  |  |
  |  |  |  |                         |    |  |  |
  |  |  |  +-------------------------+    |  |  |
  |  |  |           Padding-bottom        |  |  |
  |  |  +---------------------------------+  |  |
  |  |              Border-bottom            |  |
  |  +-------------------------------------- +  |
  |                 Margin-bottom               |
  +---------------------------------------------+



Color RGB Values:
  Decimal RGB
    3 values one for Red, one for Green, one for Blue.
    Each are 1 byte with values from 0 - 255
      rgb(0,0,0)--> Black
      rgb(255,0,0)--> Red 
      rgb(0,255,0)--> Green
      rgb(0,0,255)--> Blue
      rgb(255,255,255) -->White

  Hexadecimal RGB
    3 values one for Red, one for Green, one for Blue.
    Each are 1 byte with values from 00 - ff
      #000000 --> Black
      #ff0000 --> Red
      #00ff00 --> Green
      #0000ff --> Blue
      #ffffff --> White
*/
```
[`Back To Top`](#cascading-style-sheets)
___

<br>

# `Selectors`

A `Selector` is a pattern used to select and style HTML elements. 
* Selectors can target elements, classes, IDs, attributes, or combinations of these.

syntax
```css
selector {
  /* Declaration Block */
}
```

<br>

example
```css
body{
  background-color: black;
}
```

<br>

[`Back To Top`](#cascading-style-sheets)
___

<br>

# `Classes`
A `CSS Class` A way to apply styles to multiple elements. 
* Define a CSS `class` with a period `.` and a name
* Attach the class to an HTML `element` with the class attribute.


syntax:
```css
.classname {
  /* Declaration Block */
}
```

example
```css
.highlight{
  color: yellow;
}
```

<br>

HTML Class Attribute
syntax:
```html
<tag class = "classname"> </tag>
```

example:

```html
<p class = "highlight"> This is a paragraph with a class attribute </p> 
```


<br>

[`Back To Top`](#cascading-style-sheets)
___

<br>

# `Pseudo-classes`
A CSS `Pseudo-class` is a keyword added to a selector to style a specific state or condition of an element.

```css
selector:pseudo-class {
  /* Declaration Block */
}
```
example:
```css
div:hover{
  background-color:aqua;
}
```


<br>

[`Back To Top`](#cascading-style-sheets)
___

<br>

# `IDs`
A `CSS ID` is similar to a class but should be unique on a page. 
* Define an ID with a hash `#` in CSS
* Attach an ID to an HTML Element with the id attribute.

syntax:
```css
#id {
  /* Declaration Block */
}
```

example:
```css
#special {
  border: 2pt solid black;
}
```

HTML ID Attribute syntax:
```html

<p id = "special"> This is a paragraph with a special attribute </p>

```
<br>

[`Back To Top`](#cascading-style-sheets)
___

<br>


# `Declarations`

A CSS `Property` an attribute of an element that you want to style. 
* Examples include color, font-size, margin, and background-color.

<br>

A CSS `Value` is the specific setting assigned to a CSS property. 
* For example, #333 is a value for the color property.

<br>

A CSS `Declaration` is the combination of a CSS `property` and its corresponding `value`. 
* Declarations are enclosed in curly braces `{}`.

<br>

syntax:

```css
selector {

    property: value;
    |--------------|
          |
      Declaration
}
```

external/internal css example:
```css 
body {
  color: #FF0000;
  background-color: rgb(0,0,0);
  font-size: 24px;
}
```

inline css example:
```html

<body style="background-color:rgb(0,0,0)"></body>
```

<br>

[`Back To Top`](#cascading-style-sheets)
___

<br>

# `Rules`
A `CSS Rule` consists of one or more declarations, associated with a selector and defines how the selected elements should be styled.

<br>

```
------------------------|
selector {              |
  property:value;       |
  property:value;       |--CSS Rule
  property:value;       |
}                       |
------------------------|
```

<br>

[`Back To Top`](#cascading-style-sheets)
___

<br>

# `Declaration Block`
A `declaration block` is a group of one or more declarations within curly braces `{}` that are apart of a CSS rule. 

```

selector {              
------------------------|
  property:value;       |
  property:value;       |--Declaration Block
  property:value;       |
------------------------|
}                       

```
<br>


<br>

[`Back To Top`](#cascading-style-sheets)
___

<br>

# `CSS Box Model`

The `CSS Box Model` describes the layout of elements as a box with content, padding, border, and margin.

```
  +---------------------------------------------+
  |                  Margin-top                 |
  |  +---------------------------------------+  |
  |  |               Border-top              |  |
  |  |  +---------------------------------+  |  |
  |  |  |            Padding-top          |  |  |
  |  |  |  +-------------------------+    |  |  |
  |  |  |  |          Content        |    |  |  |
  |  |  |  |                         |    |  |  |
  |  |  |  +-------------------------+    |  |  |
  |  |  |           Padding-bottom        |  |  |
  |  |  +---------------------------------+  |  |
  |  |              Border-bottom            |  |
  |  +-------------------------------------- +  |
  |                 Margin-bottom               |
  +---------------------------------------------+
```

<br>

[`Back To Top`](#cascading-style-sheets)
___

<br>

# `RGB Color Values`
Colors can be described as a destinct set of 3 values, red, green, and blue. 
RGB values use decimal or hexadecimal numbers to define a specific color. 


<br>

## `Decimal RGB`
3 values one for Red, one for Green, one for Blue.
Each are 1 byte with values from 0 - 255

| RGB Value          | Color  |
|--------------------|--------|
| rgb(0,0,0)         | Black  |
| rgb(255,0,0)       | Red    |
| rgb(0,255,0)       | Green  |
| rgb(0,0,255)       | Blue   |
| rgb(255,255,255)   | White  |



<br>


## `Hexadecimal RGB`
3 values one for Red, one for Green, one for Blue.
Each are 1 byte with values from 00 - ff

| Hex Value   | Color  |
|-------------|--------|
| #000000     | Black  |
| #ff0000     | Red    |
| #00ff00     | Green  |
| #0000ff     | Blue   |
| #ffffff     | White  |



<br>

[`Back To Top`](#cascading-style-sheets)
___

<br>




```css
/* Resetting default margin and padding for all elements(*) */
* {
   margin: 0;
   padding: 0;
   box-sizing: border-box;
 }
 
 /* Applying styles to the body element */
 body {
   font-family: Arial, sans-serif; /* Setting the default font family */
   line-height: 1.6; /* Setting the line height for better readability */
   background-color: #f2f2f2; /* Setting the background color for the entire page */
   color: #333; /* Setting the default text color */
 }
 
 /* Styling the header element */
 h1 {
   color: #0066cc; /* Setting the color of level 1 headings */
 }
 
 /* Styling paragraphs */
 p {
   font-size: 16px; /* Setting the font size for paragraphs */
   color: #666; /* Setting the default text color for paragraphs */
   margin-bottom: 15px; /* Adding bottom margin for spacing between paragraphs */
 }
 
 /* Styling links */
 a {
   color: #0066cc; /* Setting the default color for links */
   text-decoration: none; /* Removing underlines from links */
 }
 
 /* Styling links on hover using a psuedo-class (:hover)*/

 a:hover {
   text-decoration: underline; /* Adding underline on hover for links */
 }
 
 /* Applying styles to a class named 'highlight' */
 .highlight {
   background-color: yellow; /* Setting background color for elements with the 'highlight' class */
   padding: 5px; /* Adding padding for better visual appearance */
 }
 
 /* Styling an element with a specific ID */
 #special-section {
   border: 1px solid #333; /* Adding a border to the element with the ID 'special-section' */
   padding: 10px; /* Adding padding for spacing inside the element */
 }
 
 /* Media query for responsive design */
 @media screen and (max-width: 600px) {
   /* Adjusting styles for smaller screens */
   body {
     font-size: 14px; /* Decreasing font size for smaller screens */
   }
 }
 ```