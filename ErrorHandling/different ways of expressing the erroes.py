#differnt ways to write except blocks
1.



except ZeroDivisionError:



2.



except ZeroDivisionError as msg:



3.



except (ZeroDivisionError, ValueError):



4.



except (ZeroDivisionError, ValueError) as msg:
