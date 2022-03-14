BEGIN;
--
-- Create model Student
--
CREATE TABLE `students_student` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, 
    `name` varchar(20) NULL, `age` integer NULL, 
    `course` varchar(20) NULL, 
    `depart` varchar(20) NULL
    );
COMMIT;
