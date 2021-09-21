from jinja2 import Template

name = input("Enter Name")
tn = Template("Hello {{ name }}")
msg = tn.render(name=name)

print(msg)

name = "Elon Musk"
age = 44

tn = Template("Hi, I'm {{name}}, and I'm {{age}}")
msg = tn.render(name = name, age = age)
print(msg)