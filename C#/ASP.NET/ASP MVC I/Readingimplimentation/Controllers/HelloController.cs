using Microsoft.AspNetCore.Mvc;
namespace YourNamespace.Controllers;     //be sure to use your own project's namespace!
    public class HelloController : Controller   //remember inheritance??
    {
        //for each route this controller is to handle:
        [HttpGet]       //type of request
        [Route("")]     //associated route string (exclude the leading /)
        public string Index()
        {
            return "Hello World from HelloController!";
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

