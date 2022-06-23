using System.Diagnostics;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using The_Wall.Models;

namespace The_Wall.Controllers;

public class HomeController : Controller
{
    private MyContext _context;

    public HomeController(MyContext context)
    {
        _context = context;
    }

    public IActionResult Dashboard()
    {
        ViewBag.userid = HttpContext.Session.GetInt32("userid");
        return View("Dashboard");
    }


    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
