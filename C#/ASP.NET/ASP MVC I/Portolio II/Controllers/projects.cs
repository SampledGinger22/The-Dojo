using Microsoft.AspNetCore.Mvc;
namespace Portolio_II.Controllers;
    public class ProjectsController : Controller
    {
        [HttpGet("/projects")]
        public ViewResult projects()
        {
            //Views/Home/HiThere.cshtml
            //Views/Shared/HiThere.cshtml
            return View();
        }
    }