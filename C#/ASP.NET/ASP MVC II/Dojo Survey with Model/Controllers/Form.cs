using Microsoft.AspNetCore.Mvc;
using Dojo_Survey_With_Model.Models;
namespace Dojo_Survey_With_Model.Controllers;
    public class HomeController : Controller
    {
        [HttpGet("")]
        public ViewResult form()
        {
            //Views/Home/HiThere.cshtml
            //Views/Shared/HiThere.cshtml
            return View();
        }
    }