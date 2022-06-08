using Microsoft.AspNetCore.Mvc;
namespace readingimplimentation.Controllers;     //be sure to use your own project's namespace!

    // The "Home" in HomeController specifies the folder it searches in first. 
    public class HomeController : Controller   //remember inheritance??
    {
        //for each route this controller is to handle:
        [HttpGet("")]       //type of request
        public ViewResult HiThere()
        {
            //Views/Home/HiThere.cshtml
            //Views/Shared/HiThere.cshtml
            return View();
        }

        //localhost:5000/hello
        [HttpGet("hello")]
        public string Hello(){
            return "Hi Again!";
        }

        //localhost:5000/users/???
        [HttpGet("users/{username}/{location}")]
        public string HelloUser(string username, string location){
            return $"Hello {username} from {location}";
        }
    }

