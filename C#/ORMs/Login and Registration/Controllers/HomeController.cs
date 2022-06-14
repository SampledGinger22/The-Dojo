using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using Login_and_Registration.Models;
using Microsoft.AspNetCore.Identity;

namespace Login_and_Registration.Controllers;

public class HomeController : Controller
{

    private MyContext _context;

    public HomeController(MyContext context)
    {
        _context = context;
    }

    [HttpGet("")]
    public IActionResult Login()
    {
        return View();
    }

    [HttpGet("/registration")]
    public IActionResult Registration()
    {
        return View();
    }

    [HttpPost("access")]
    public IActionResult Access(User userSubmission)
    {
        if(HttpContext.Session.GetInt32("userid") != null){
            return RedirectToAction("Index");
        }
        if(ModelState.IsValid)
        {
            var userInDb = _context.Users.FirstOrDefault(u => u.Email == userSubmission.Email);
            if(userInDb == null)
            {
                ModelState.AddModelError("Email", "Invalid Email/Password");
                return View("login");
            }
            else 
            {
                var hasher = new PasswordHasher<User>();
                var result = hasher.VerifyHashedPassword(userSubmission, userInDb.Password, userSubmission.Password);
                if(result == 0)
                {
                    ModelState.AddModelError("Email", "Invalid Email/Password");
                    return View("login");
                }
                else {
                    if(HttpContext.Session.GetInt32("userid") == null)
                    {
                        HttpContext.Session.SetInt32("userid", userSubmission.id);
                    }
                    return View("Index");
                }
            }
        }
        else
        {
            ModelState.AddModelError("Email", "Something went wrong");
            return View("login");
        }
    }

    [HttpPost("register")]
    public IActionResult Register(User user)
    {
        HttpContext.Session.Clear();
        if(ModelState.IsValid)
        {
            if(_context.Users.Any(u => u.Email == user.Email))
            {
                ModelState.AddModelError("Email", "Email is already in use!");
                return RedirectToAction("registration");
            }
            else
            {
                PasswordHasher<User> Hasher = new PasswordHasher<User>();
                user.Password = Hasher.HashPassword(user, user.Password);
                _context.Add(user);
                _context.SaveChanges();
                var newuser = _context.Users.FirstOrDefault(u => u.Email == user.Email);
                if(HttpContext.Session.GetInt32("userid") == null && newuser != null)
                {
                    HttpContext.Session.SetInt32("userid", newuser.id);
                }
                return RedirectToAction("index");
            }
        }
        else
        {
            return RedirectToAction("registration");
        }  
    }
    [HttpGet("success")]
    public IActionResult Index()
    {
        if(HttpContext.Session.GetInt32("userid") == null)
        {
            return RedirectToAction("login");
        }
        else return View("Index");
    }

    [HttpGet("logout")]
    public IActionResult logout()
    {
        HttpContext.Session.Clear();
        return RedirectToAction("login");
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
