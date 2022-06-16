using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using Wedding_Planner.Models;
using Microsoft.AspNetCore.Identity;

namespace Wedding_Planner.Controllers;

public class LoginController : Controller
{

    private MyContext _context;

    public LoginController(MyContext context)
    {
        _context = context;
    }

    [HttpGet("")]
    public IActionResult LoginandReg()
    {
        return View();
    }

    [HttpPost("access")]
    public IActionResult Access(UserInLogin userSubmission)
    {
        if(HttpContext.Session.GetInt32("userid") != null){
            return RedirectToAction("Dashboard");
        }
        if(ModelState.IsValid)
        {
            var userInDb = _context.Users.FirstOrDefault(u => u.Email == userSubmission.Email);
            if(userInDb == null)
            {
                ModelState.AddModelError("Email", "Invalid Email/Password");
                return View("LoginandReg");
            }
            else 
            {
                var hasher = new PasswordHasher<User>();
                var result = hasher.VerifyHashedPassword(userInDb, userInDb.Password, userSubmission.Password);
                if(result == 0)
                {
                    ModelState.AddModelError("Email", "Invalid Email/Password");
                    return View("LoginandReg");
                }
                else {
                    if(HttpContext.Session.GetInt32("userid") == null)
                    {
                        HttpContext.Session.SetInt32("userid", userInDb.UserId);
                    }
                    return View("LoginandReg");
                }
            }
        }
        else
        {
            ModelState.AddModelError("Email", "Something went wrong");
            return View("LoginandReg");
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
                return RedirectToAction("LoginandReg");
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
                    HttpContext.Session.SetInt32("userid", newuser.UserId);
                }
                return RedirectToAction("LoginandReg");
            }
        }
        else
        {
            return RedirectToAction("LoginandReg");
        }  
    }

    [HttpGet("logout")]
    public IActionResult logout()
    {
        HttpContext.Session.Clear();
        return RedirectToAction("LoginandReg");
    }
}