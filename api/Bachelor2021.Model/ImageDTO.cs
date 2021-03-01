using Microsoft.AspNetCore.Http;
using System;
using System.Collections.Generic;
using System.Text;

namespace Bachelor2021.Model {
    public class ImageDTO {
        public string FileName { get; set; }

        public IFormFile Image { get; set; }
    }
}
