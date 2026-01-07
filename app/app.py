from fastapi import FastAPI

app = FastAPI()

thePosts = {
    1:{
        "title":"Some shit",
        "content":"This is some shit.",
        "author":"Pukar Pandey"
    },
    2:{
        "title":"Some shit",
        "content":"This is some shit.",
        "author":"Pukar Pandey"
    },
    3:{
        "title":"Some shit",
        "content":"This is some shit.",
        "author":"Pukar Pandey"
    },
    4:{
        "title":"Some shit",
        "content":"This is some shit.",
        "author":"Pukar Pandey"
    },
    5:{
        "title":"Some shit",
        "content":"This is some shit.",
        "author":"Pukar Pandey"
    }
}

@app.get("/posts")
def getAllPosts():
    return thePosts
