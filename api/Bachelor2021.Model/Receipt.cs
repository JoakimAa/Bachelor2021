using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace Bachelor2021.Model {
    public class Receipt {
        [Key]
        public int ReceiptId { get; set; }
        [Required]
        public double Amount { get; set; }
        [Required]
        public string Type { get; set; }
        [Required]
        public string Company { get; set; }
        [Required]
        public string Date { get; set; }
        public int ImageId { get; set; }
    }
}

