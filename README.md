# Health Gate Blog
The purpose of creating this health blog, is to facilitate for authors to share their knowlledge and experiences with others. Authors add their research, opinion and such to the larger wealth of health information. It could be based on real-life experiences, where the author wants a platform to communicate with others of similar concerns.
# Features:
## Existing Features:
### Home page:

![image](https://user-images.githubusercontent.com/91415085/212841361-0f1208ef-bf5d-4ebc-b420-6b6f00ebc77d.png)

- The home page feature has the main nav bar whcih include:
* The home page link
* The Registration link that ask users to sign up in order to become a part of the community and be able to post thier blogs in the website, also to comments, like, and vote on other posts:

![image](https://user-images.githubusercontent.com/91415085/212843153-143d48c0-ff08-445f-85cd-e0a99b901829.png)

* The login icon, which next to the registration icon:
- After registeration, you can sign in with username and password:

![image](https://user-images.githubusercontent.com/91415085/212843856-80b1fe0d-2426-4de4-94c8-ed4406e20ef0.png)

* Once logged in, you have the facility to add a post as an author after clicking on the add post icon next to home icon. Also you have the ability to comments on other posts, like, or vote:
![image](https://user-images.githubusercontent.com/91415085/212845012-a3f7378c-aef9-4e95-a6ff-1c08475b0c6e.png)
![image](https://user-images.githubusercontent.com/91415085/212845268-00502681-3de0-4d4e-8424-6a7a44412dc6.png)

* You can edit or delete your own posts, the facility to update or delete are showing oneach post on either on the main page:
![image](https://user-images.githubusercontent.com/91415085/212847031-bfa967d6-6911-4726-9556-3e550cdda8b7.png)

Or when click on the categories of each post:
![image](https://user-images.githubusercontent.com/91415085/212847408-9f6bb0d1-5f3c-4eec-bd5c-7cb059fc7fdf.png)

* By clicking on Edit or Delete buttons, you will come accross these two pages:
![image](https://user-images.githubusercontent.com/91415085/212848569-c2f00050-cf23-4fbb-a625-dfc7a7fddfc6.png)
![image](https://user-images.githubusercontent.com/91415085/212848809-1b8d2727-5938-4bb9-8576-cf29aa1a44c2.png)

- These CRUD functionality will allow users to create, read, update, and delete their own posts, and prevent others from doing that.

### Categories Feature:
The home page contains a minimum of 6 posts from diffirent categories
- There are 4 Categories at the moments:
* Niutrition
* Meditation
* Health
* Exercise
You can find on each category there related subjects
- I have created costum model which was inspired from the walkthrough project 5, then I have created a code in the template to link the view and the home url with index page. I have also used bootsrap style, and added the css style in style section in the index page.

### Posts Feature:
![image](https://user-images.githubusercontent.com/91415085/212850658-291aac43-deff-483d-8cca-980eb894dc9b.png)
Each post has the comment section, and the reply to comments secion, also has the like, and vote icons in order for the users to interact with the author:
![image](https://user-images.githubusercontent.com/91415085/212851555-6ea7c5ba-5633-4ea1-abd3-451c6b428faa.png)

* In the post section I have created the upvote and downvote buttons, I have used similar strucure for the code used in previous walkthrough codestar project, and added two variables in the Post model and created the view for both of them and linked it to the urls,a and update the post-detail template accordingly, in order to help the users to share thier opinion about the post with the author.

### Comments Feature:
* I have added a success message to the Post Detail view when a user leaves a comment that will let the user know that their comment is awaiting approval, and it will auto-dismiss after 3 seconds:
![image](https://user-images.githubusercontent.com/91415085/212863122-3ada6acd-fe1c-4280-9936-790b413ba176.png)


### Reply to Comments Feature:
I have added a parent variable and the childern function to the Comment model, and linked them to each other by using the decorator, I have create the view, and created JavaScript code to toggle the reply to comment box icon in the template and linked it with the urls.


## Future features to be added;
* The ability to edit, and delete reviews functionalities to commments and reply to comments 
* The ability to submit testimonials
* The ability to add videos
* The ability to add like, vote functionalities to comments and reply to comments 
* The ability to add multibe replies functionalities to the comments 
* The ability to create a user profile and follow/unfollow other users


## Bugs:
No bugs

## Fixed Bugs:

In the categories feature:
### I had e a bug when I was trying to add the bootstrap css style to the categories in the style.css, it didn't apply, and I wanted to get rid of the issue:
![image](https://user-images.githubusercontent.com/91415085/212871201-2d095baa-a0a3-4636-aa2d-e6fb0468268e.png)

### I have manged to solve the issue by adding the style section to the index page:
![image](https://user-images.githubusercontent.com/91415085/212871500-e4957d32-9583-4057-bc20-3af4ebee07f6.png)


## Testing:
I have done testing to my code and checked all the features are working efficiently.

## Deployment:
This project was deployed using Code Institute's mock terminal for Heroku

##### Steps for deployment:

* Fork or clone this repository
* Create a new Heroku app
* Link the Heroku app to the repository
* Click on deploy:
Link to Heroku app:
https://health-gate.herokuapp.com/

## Credits: 

* Code Institute for the deployment terminal
* Code Institute for the Walkthrough Project 4
* Building a social media web app tutorials on YouTube:
https://www.youtube.com/watch?v=Rpi0Ne1nMdk&list=PLPSM8rIid1a3TkwEmHyDALNuHhqiUiU5A
https://www.youtube.com/watch?v=J7xaESAddDQ
