using Microsoft.AspNetCore.Mvc;
using ViewModel_Fun.Models;
namespace ViewModel_Fun.Controllers;
    public class UsersController : Controller
    {
        [HttpGet("/users")]
        public IActionResult users()
        {
            List<User> userslist = new List<User>();
                userslist.Add(new Models.User("Moose", "Philips"));
                userslist.Add(new Models.User("Sarah"));
                userslist.Add(new Models.User("Jerry"));
                userslist.Add(new Models.User("Rene", "Ricky"));
                userslist.Add(new Models.User("Barbarah"));
            return View("users", userslist);
        }

        [HttpGet("/user")]
        public IActionResult user()
        {
            List<User> userslist = new List<User>();
                userslist.Add(new Models.User("Moose", "Philips"));
                userslist.Add(new Models.User("Sarah"));
                userslist.Add(new Models.User("Jerry"));
                userslist.Add(new Models.User("Rene", "Ricky"));
                userslist.Add(new Models.User("Barbarah"));
            return View("User", userslist);
        }
    }