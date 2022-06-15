using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Products_and_Categories.Models;

namespace Products_and_Categories.Controllers;

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
        return RedirectToAction("Categories");
    }

    [HttpGet("categories/view/{CategoryId}")]
    public IActionResult CategoryView(int CategoryId)
    {
        var category = _context.Categories
            .Include(t => t.CatAssociations)
                .ThenInclude(sub => sub.ProductId)
            .FirstOrDefault(c => c.CategoryId == CategoryId);
            
        return View("Index", category);
    }

    [HttpGet("products")]
    public IActionResult Products()
    {
        return View("Products");
    }

    [HttpGet("categories")]
    public IActionResult Categories()
    {
        List<Category> categories = _context.Categories.ToList();
        ViewBag.categories = categories;
        
        return View("Categories");
    }

    [HttpPost("categories/save/new")]
    public IActionResult SaveCategory(Category category)
    {
        _context.Add(category);
        _context.SaveChanges();
        return RedirectToAction("Categories");
    }

    [HttpGet("products/view/{ProductId}")]
    public IActionResult ViewProd(int ProdId)
    {
        return View("ViewProd");
    }



    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
