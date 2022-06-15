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
        List<Chef> chefList = _context.Chefs
            .Include(d => d.newDishes)
            .ToList();

        return View("Index", chefList);
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

    [HttpPost("newchef/save")]
    public IActionResult SaveChef(Chef newChef)
    {
        if(ModelState.IsValid)
        {
            _context.Add(newChef);
            _context.SaveChanges();
            return RedirectToAction("Index");
        }
        else 
        {
            return View("NewChef");
        }
    }

    [HttpGet("newdish")]
    public IActionResult NewDish()
    {
        List<Chef> allChefs = _context.Chefs.ToList();
        ViewBag.Chefs = allChefs;
        return View("NewDish");
    }

    [HttpPost("newdish/save")]
    public IActionResult SaveDish(Dish newDish)
    {
        if(ModelState.IsValid)
        {
            _context.Add(newDish);
            _context.SaveChanges();
            return RedirectToAction("Dishes");
        }
        else 
        {
            return View("NewDish");
        } 
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
