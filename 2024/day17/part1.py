class Registers:
    A = 0
    B = 0
    C = 0

class Computer:
    def __init__(self, program:list[int]) -> None:
        self.registers = Registers()
        self.program = program
        self.outputs = []
        self.instruction_current = 0
        self.instruction_next = 2
        self.operations = [
            self.adv,
            self.bxl,
            self.bst,
            self.jnz,
            self.bxc,
            self.out,
            self.bdv,
            self.cdv
        ]

    def set_regs(self, a:int, b:int, c:int) -> None:
        """set register defaults"""
        self.registers.A = a
        self.registers.B = b
        self.registers.C = c

    def run_program(self) -> list[str]:
        """run the program"""
        self.outputs = []
        while self.instruction_current < len(self.program):
            opc, opa = self.get_instruction()
            if opc == 5:
                # opcode 5 has a return value
                self.outputs.append((self.operations[opc])(opa))
            else:
                (self.operations[opc])(opa)
            self.next_instruction()
        return self.outputs

    def next_instruction(self) -> None:
        """set instruction pointer"""
        self.instruction_current = self.instruction_next
        self.instruction_next += 2

    def get_instruction(self) -> tuple[int,int]:
        """fetch the current instruction"""
        opc_opa = (
            self.program[self.instruction_current],
            self.program[self.instruction_current + 1]
        )
        return opc_opa

    def combo(self, operand:int) -> int:
        """return combo value as a literal"""
        if operand <= 3:
            return operand
        if operand == 4:
            return self.registers.A
        if operand == 5:
            return self.registers.B
        if operand == 6:
            return self.registers.C
        # should never reach here
        return 0

    def adv(self, operand:int) -> None:
        """opcode 0"""
        self.registers.A //= 2**self.combo(operand)

    def bxl(self, operand:int) -> None:
        """opcode 1"""
        self.registers.B ^= operand

    def bst(self, operand:int) -> None:
        """opcode 2"""
        self.registers.B = self.combo(operand) % 8

    def jnz(self, operand:int) -> None:
        """opcode 3"""
        if self.registers.A != 0:
            self.instruction_next = operand

    def bxc(self, operand:int) -> None: # pylint:disable=W0613
        """opcode 4"""
        self.registers.B ^= self.registers.C

    def out(self, operand:int) -> int:
        """opcode 5"""
        return self.combo(operand) % 8

    def bdv(self, operand:int) -> int:
        """opcode 6"""
        self.registers.B = self.registers.A // 2**self.combo(operand)

    def cdv(self, operand:int) -> int:
        """opcode 7"""
        self.registers.C = self.registers.A // 2**self.combo(operand)

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        reg, prog = f.read().split("\n\n", maxsplit=1)

    regs = [int(line.split(": ", maxsplit=1)[1]) for line in reg.split("\n")]

    program = list(map(int, prog.removeprefix("Program: ").split(",")))
    computer = Computer(program)
    computer.set_regs(*regs)

    output = computer.run_program()
    print(",".join(map(str, output)))

if __name__ == "__main__":
    main()
