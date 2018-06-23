
This week, I will give some examples of the [object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming) part of Python. The object-oriented programming has [many advantages](https://www.quora.com/What-are-the-benefits-of-object-oriented-programming). And I really like them due to the reusability of the code and the feeling of modeling the world :-). I will give some examples that I usually use in my code as a quick guide of how to use these in your code. This tutorial serves as a quick guide, if you want to learn more, you should go to the [documentation](https://docs.python.org/3/tutorial/classes.html). 


### Define a class
Let's start to look at the following examples, where we create a People class. 


```python
class People(object):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print("Greetings, " + self.name)
```

Typical python class has a constructor, that is the \__init\__() function, which initializes the class when you call it. This means that, when you first initialize your class, this function will be only run once. The 'self' means the instance itself, you can find a very [good explanation here](https://pythontips.com/2013/08/07/the-self-variable-in-python-explained/). The self.name and self.age are the attributes that the class will have, you can see from the following example. And the greet function is the method that we define in the class. Let's see how we can actually use it.   


```python
person1 = People(name = 'Iron Man', age = 35)
person1.greet()
print(person1.name)
```

    Greetings, Iron Man
    Iron Man


### Inheritance

One of the most important features of using the object-oriented programming is that we can easily reuse the code above to create some new classes. For example, we want to have another class Teacher that have all the attributes and methods People class have, but at the same time, we want to have more new methods. 


```python
class Teacher(People):
    
    def teach_students(self, x, y):
        print('x + y = %d'%(x+y))
```


```python
teacher1 = Teacher(name = 'Susan', age = 24)
teacher1.greet()
teacher1.teach_students(x = 3, y = 5)
```

    Greetings, Susan
    x + y = 8


We can see from the above code that, we don't need to re-define all the attributes and greet function, the Teacher class actually have all these from People class, this is due to this line: **class Teacher(People)**, which basically say that we want Teacher class to get all the things from People class. This is called inherit, and class Teacher inherits from class People. And People is the parent class and Teacher is a child class. And then we could extend the methods in class Teacher by just define new functions. Or if we want to replace some of the old methods in People, all we need to do is to re-define the function, for example, in the following lines, we replace the greet method in People with a new one that greet the teacher. 


```python
class Teacher(People):
    
    def greet(self):
        print("Greetings, teacher: " + self.name)
    
    def teach_students(self, x, y):
        print('x + y = %d'%(x+y))
```


```python
teacher1 = Teacher(name = 'Susan', age = 24)
teacher1.greet()
```

    Greetings, teacher: Susan


### The super method

Also, often times, we want to expand the constructor by having more attributes and so on, but at the same time, we don't want to re-type all the code as before, therefore, we could use the super method to avoid referring to the parent class explicitly. Let's see below that we want to add a studentId field into the Student class. 


```python
class Student(People):
    def __init__(self, name, age, studentId):
        super().__init__(name, age)
        self.studentId = studentId
```


```python
student1 = Student(name = 'Kevin', age = 20, studentId = '12345')
print('Student %s has id as %s'%(student1.name, student1.studentId))
```

    Student Kevin has id as 12345


### Multiple inheritances

What if we have a student_teacher class that we want to inherit from both Teacher and Student class. Easy, you can just do the following:


```python
class Student_Teacher(Teacher, Student):
    pass
```


```python
st1 = Student_Teacher(name = 'Kate', age = 23, studentId = '54321')
print('Teacher %s has studentId as %s'%(st1.name, st1.studentId))
st1.teach_students(3,6)
```

    Teacher Kate has studentId as 54321
    x + y = 9

