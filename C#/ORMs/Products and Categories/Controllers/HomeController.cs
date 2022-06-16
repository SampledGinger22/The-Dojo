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
        Category? category = _context.Categories.FirstOrDefault(c => c.CategoryId == 1);
        if(category == null)
        {
            return RedirectToAction("Categories");
        }
        return Redirect("categories/view/1"); 
    }

    [HttpGet("categories/view/{CatId}")]
    public IActionResult CategoryView(int CatId)
    {
        var categoryMain = _context.Categories
            .Include(t => t.CategoryProds)
                .ThenInclude(sub => sub.product)
            .FirstOrDefault(c => c.CategoryId == CatId);

        ViewBag.unallocatedprods = _context.Products
            .Include(a => a.ProdCategories)
            .Where(c => !c.ProdCategories.Any(c => c.CategoryId == CatId));

        ViewBag.CatId = CatId;
        return View("Index", categoryMain);
    }

    [HttpPost("categories/update/{Id}")]
    public IActionResult UpdateProdAssociation(Association newAssoc, int Id)
    {
        newAssoc.CategoryId = Id;
        _context.Associations.Add(newAssoc);
        _context.SaveChanges();
        return RedirectToAction("Categories");
    }

    [HttpGet("products/view/{ProjId}")]
    public IActionResult ProjectView(int ProjId)
    {
        var projectMain = _context.Products
            .Include(t => t.ProdCategories)
                .ThenInclude(sub => sub.category)
            .FirstOrDefault(c => c.ProductId == ProjId);

        ViewBag.unallocatedcats = _context.Categories
            .Include(a => a.CategoryProds)
            .Where(c => !c.CategoryProds.Any(c => c.ProductId == ProjId));

        ViewBag.CatId = ProjId;
        return View("Index", projectMain);
    }

    [HttpPost("projects/update/{Id}")]
    public IActionResult UpdateCatAssociation(Association newAssoc, int Id)
    {
        newAssoc.ProductId = Id;
        _context.Associations.Add(newAssoc);
        _context.SaveChanges();
        return RedirectToAction("Products");
    }

    [HttpGet("products")]
    public IActionResult Products()
    {
        List<Product> products = _context.Products.ToList();
        ViewBag.products = products;
        
        return View("Products");
    }

    [HttpPost("products/save/new")]
    public IActionResult SaveProduct(Product product)
    {
        if(ModelState.IsValid)
        {
            _context.Products.Add(product);
            _context.SaveChanges();
            return RedirectToAction("Products");
        }
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
        if(ModelState.IsValid)
        {
            _context.Add(category);
            _context.SaveChanges();
            return RedirectToAction("Categories");
        }
        return View("Categories");
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
