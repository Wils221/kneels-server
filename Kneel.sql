CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `STYLES`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `SIZES`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NUMERIC(4,2) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);


INSERT INTO `Metals` VALUES (null, "Sterling Silver", 12.42);
INSERT INTO `Metals` VALUES (null, "14K Gold", 736.40);
INSERT INTO `Metals` VALUES (null, "24K Gold", 1258.90);
INSERT INTO `Metals` VALUES (null, "Platinum", 795.45);
INSERT INTO `Metals` VALUES (null, "Palladium", 1241.00);

INSERT INTO `Sizes` VALUES (null, "0.5", 500.00);
INSERT INTO `Sizes` VALUES (null, "0.75", 1000.00);
INSERT INTO `Sizes` VALUES (null, "1", 1500.00);
INSERT INTO `Sizes` VALUES (null, "1.5", 2000.00);
INSERT INTO `Sizes` VALUES (null, "2", 3500.00);

INSERT INTO `Styles` VALUES (null, "Classic", 500.00);
INSERT INTO `Styles` VALUES (null, "Modern", 710.00);
INSERT INTO `Styles` VALUES (null, "Vintage", 965.00);

CREATE TABLE `Orders` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    FOREIGN KEY (`metal_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY (`style_id`) REFERENCES `Styles`(`id`),
    FOREIGN KEY (`size_id`) REFERENCES `Sizes`(`id`)
);
ALTER TABLE Orders
ADD timestamp FLOAT;

UPDATE Orders
SET timestamp = 1614659931693;

INSERT INTO `Orders` VALUES (null, 1, 2, 3);
INSERT INTO `Orders` VALUES (null, 2, 3, 4);
INSERT INTO `Orders` VALUES (null, 3, 1, 5);
INSERT INTO `Orders` VALUES (null, 4, 2, 1);
INSERT INTO `Orders` VALUES (null, 5, 3, 2);

SELECT * FROM `Orders`

SELECT
    o.size_id,
    o.style_id,
    o.metal_id,
    m.metal,
    m.price metal_price,
    s.style,
    s.price style_price,
    sz.carets,
    sz.price size_price
FROM `Orders` o
JOIN `Metals` m ON m.id = o.metal_id
JOIN styles s ON s.id = o.style_id
JOIN sizes sz ON sz.id = o.size_id



