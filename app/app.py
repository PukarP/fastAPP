from fastapi import FastAPI,HTTPException
from app.schemas import CreatePost
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

#this is for like a particular post you click on

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in thePosts:
        raise HTTPException(status_code=404, detail="Item not found")
    return thePosts.get(id)

@app.post("/posts")
def createPost(post: CreatePost):
    newPost = {"title": post.title,"content": post.content,"author": post.author}
    thePosts[max(thePosts.keys())+1] = newPost
    return {"message": "New thingy added successfully"}

