using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using Chefs_n_Dishes.Models;
using Microsoft.EntityFrameworkCore;

namespace Chefs_n_Dishes.Controllers;

public class HomeController : Controller
{
    private MyContext _context;

    public HomeController(MyContext context)
    {
        _context = context;
    }

    [HttpGet("")]
    public IActionResult Index()
    {
        List<Dish> userDishes = _context.Dishes.Include(d => d.Creator).ToList();

        return View("Index", userDishes);
    }

    [HttpGet("dishes")]
    public IActionResult Dishes()
    {
        List<Dish> userDishes = _context.Dishes.Include(d => d.Creator).ToList(); 

        return View("dishes", userDishes);
    }

    [HttpGet("newchef")]
    public IActionResult NewChef()
    {
        return View();
    }

    [HttpGet("newdish")]
    public IActionResult NewDish()
    {
        return View();
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
