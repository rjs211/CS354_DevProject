# CS354_DevProject
Course Project for CS354 DBMS


The project aims to build a tool with web interface for automatic form flling of details from a database.
The forms are available in ODF format (.odt) with formatted placeholders with delimiters at the beginning and end of the placeholder.  These placeholders will be replaced by data specific to the user.  

The data specific to the user will be if not availble, will be requested from the user through a dynamically generated form.  Once aquired, that information is saved in the corresponding field and never asked again.

The project is meant to have two parallel implementations. 
1. PHP 7
1. Django
