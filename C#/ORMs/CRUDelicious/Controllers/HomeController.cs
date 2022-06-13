using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using CRUDelicious.Models;

namespace CRUDelicious.Controllers;

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
        List<Dish> AllDishes  =_context.Dishes.OrderBy(c => c.CreatedAt).ToList();

        return View(AllDishes);
    }

    [HttpGet("view/dish/{DishId}")]
    public IActionResult ViewDish(int DishId)
    {
        Dish dish = _context.Dishes.First(d => d.DishId == DishId);
        return View("view", dish);
    }

    [HttpGet("edit/dish/{DishId}")]
    public IActionResult Edit(int DishId)
    {
        Dish dish = _context.Dishes.First(d => d.DishId == DishId);
        return View("edit", dish);
    }

    public IActionResult updatedish(int DishId)
    {
        Dish update = _context.Dishes.Update(d => d.DishId = DishId)
        return Redirect("Index");
    }
    public IActionResult Create()
    {
        return View();
    }

    

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
