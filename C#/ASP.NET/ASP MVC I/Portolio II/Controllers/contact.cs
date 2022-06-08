using Microsoft.AspNetCore.Mvc;
namespace Portolio_II.Controllers;
    public class ContactController : Controller
    {
        [HttpGet("/contact")]
        public ViewResult contact()
        {
            //Views/Home/HiThere.cshtml
            //Views/Shared/HiThere.cshtml
            return View();
        }
    }