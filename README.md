# 

## Languages and Tools

<a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a><a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a>
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a>
<a href="https://www.typescriptlang.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/typescript/typescript-original.svg" alt="typescript" width="40" height="40"/> </a>
<a href="https://reactjs.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/> </a>
<a href="https://www.figma.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/figma/figma-icon.svg" alt="figma" width="40" height="40"/> </a>
<a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a>
<a href="https://www.python.org/" target="_blank" rel="noreferrer" ><img src="https://www.vectorlogo.zone/logos/python/python-icon.svg" alt="python" width="40" height="40"/></a>
<a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer" ><img src="https://www.vectorlogo.zone/logos/djangoproject/djangoproject-icon.svg" alt="django" width="40" height="40"/></a>
<a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer" ><img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/></a>
<a href="https://www.sqlite.org/" target="_blank" rel="noreferrer" ><img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/></a>
<a href="https://www.mysql.com/" target="_blank" rel="noreferrer" ><img src="https://www.vectorlogo.zone/logos/mysql/mysql-icon.svg" alt="mysql" width="40" height="40"/></a>

def new_format(string):
    res = []
    res+=''.join(reversed(string))
    print(res)
    i =0
    for i in range(len(res)):
        i += 1
        if i % 3 == 0:
            res[i] +=(',')
    print(res)
    res.reverse()
    result =""
    for i in range(len(res)):
        result += res[i]
    print(result)
    return result



