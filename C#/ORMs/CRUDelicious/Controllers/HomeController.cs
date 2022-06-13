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
        Dish? dish = _context.Dishes.FirstOrDefault(d => d.DishId == DishId);

        return View("edit", dish);
    }

    [HttpPost("dish/update")]
    public IActionResult updatedish(int DishId, Dish plate)
    {
        Dish? dish = _context.Dishes.FirstOrDefault(d => d.DishId == DishId);
        if(ModelState.IsValid) 
        {
            if(dish != null)
            {
                dish.Name = plate.Name;
                dish.Chef = plate.Chef;
                dish.Tastiness = plate.Tastiness;
                dish.Calories = plate.Calories;
                dish.Description = plate.Description;
                dish.UpdatedAt = DateTime.Now;
            }
            _context.SaveChanges();
            return RedirectToAction("ViewDish", dish);
        }
        else 
        {
            return View("edit", dish);
        }
    }

    [HttpGet("create")]
    public IActionResult Create()
    {
        return View();
    }

    [HttpPost("dish/new")]
    public IActionResult SaveNew(Dish plate)
    {
        if(ModelState.IsValid)
        {
            _context.Add(plate);
            _context.SaveChanges();
            return RedirectToAction("ViewDish", plate);
        }
        else
        {
            return View("Create");
        }
    }

    [HttpGet("delete/dish/{DishId}")]
    public IActionResult Delete(int DishId)
    {
        Dish? dish = _context.Dishes.FirstOrDefault(d => d.DishId == DishId);
        if(dish != null)
        {
            _context.Dishes.Remove(dish);
            _context.SaveChanges();
        }
        return RedirectToAction("Index");
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
