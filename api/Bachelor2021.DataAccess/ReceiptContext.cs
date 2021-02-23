using Bachelor2021.Model;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;
using System;

namespace Bachelor2021.DataAccess {
    public class ReceiptContext : DbContext {

        public DbSet<Receipt> Receipts { get; set; }
        public ReceiptContext(DbContextOptions<ReceiptContext> options) : base(options) { }

        class DataContextFactory : IDesignTimeDbContextFactory<ReceiptContext> {
            public ReceiptContext CreateDbContext(string[] args) {
                var connection = @"Server=(localdb)\MSSQLLocalDB;Database=Bachelor2021;Trusted_Connection=True;ConnectRetryCount=0";

                var optionsBuilder = new DbContextOptionsBuilder<ReceiptContext>();
                optionsBuilder.UseSqlServer(connection, x => x.MigrationsAssembly("Bachelor2021.DataAccess.Maintenance"));

                return new ReceiptContext(optionsBuilder.Options);
            }
        }
    }
}
