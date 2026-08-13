from abc import ABC
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Union


@dataclass
class Expression(ABC):
    pass


@dataclass
class Factor(Expression, ABC):
    pass


@dataclass
class UnaryExpr(Expression):
    operation: str | None = field(default=None)
    sub_expression: Union["ExpressionType", None] = field(default=None)


@dataclass
class CompoundExpr(Expression):
    operation: str | None = field(default=None)
    sub_expressions: list["ExpressionType"] | None = field(default_factory=list)


@dataclass
class PathEl:
    kind: str | None = field(default=None)
    ref: str | None = field(default=None)
    num_index: int | None = field(default=None)
    spec_index: str | None = field(default=None)


@dataclass
class PathOrInspFactor(Factor):
    path_els: list[PathEl] = field(default_factory=list)
    inspection: str | None = field(default=None)


@dataclass
class EnumAssignment:
    # reference to Ilismeta16.EnumNode
    min_enum_value: str = field()
    max_enum_value: str | None = field(
        default=None,
    )
    value_to_assign: Union["ExpressionType", None] = field(
        default=None,
    )


@dataclass
class EnumMapping(Factor):
    enum_value: PathOrInspFactor | None = field(
        default=None,
    )
    cases: list[EnumAssignment] = field(
        default_factory=list,
    )


@dataclass
class ActualArgument:
    kind: str = field()
    # reference string to Argument
    formal_argument: str | None = field(
        default=None,
    )
    # references to classes bag {0..1}
    expression: Union["ExpressionType", None] = field(
        default=None,
    )
    # references to classes bag {0..*}
    object_classes: list[str] = field(
        default_factory=list,
    )


@dataclass
class FunctionCall(Factor):
    # ref to IlisMeta16.FunctionDef
    function: str | None = field(
        default=None,
    )
    arguments: list[ActualArgument] = field(
        default_factory=list,
    )


@dataclass
class RuntimeParamRef(Factor):
    # reference to Ilismeta16.AttrOrParam
    runtime_param: str = field()


@dataclass
class Constant(Factor):
    value: str = field()
    type: str = field()


@dataclass
class ClassConst(Factor):
    # reference to Ilismeta16.Class
    class_value: str | None = field(default=None)


@dataclass
class AttributeConst(Factor):
    # reference to Ilismeta16.AttrOrParam
    attribute: str | None = field(default=None)


@dataclass
class UnitRef(Factor):
    unit: str | None = field(default=None)


@dataclass
class UnitFunction(Factor):
    explanation: str = field()


@dataclass
class ExpressionType:
    class Meta:
        global_type = False

    choice: (
        UnitFunction
        | UnitRef
        | AttributeConst
        | ClassConst
        | Constant
        | RuntimeParamRef
        | FunctionCall
        | EnumMapping
        | PathOrInspFactor
        | CompoundExpr
        | UnaryExpr
        | None
    ) = field(default=None)


@dataclass
class Constraint:
    id: str = field()
    name: str = field()
    documentation: list[str] = field()
    to_class: str | None = field(default=None)
    to_domain: str | None = field(default=None)


@dataclass(kw_only=True)
class SimpleConstraint(Constraint):
    kind: str = field()
    percentage: Decimal | None = field(
        default=None,
    )
    logical_expression: ExpressionType | None = field(default=None)


@dataclass(kw_only=True)
class ExistenceConstraint(Constraint):
    attr: PathOrInspFactor = field()


@dataclass(kw_only=True)
class UniqueConstraint(Constraint):
    kind: str = field()
    unique_def: list[PathOrInspFactor] = field()
    # bag of...
    where: ExpressionType | None = field(default=None)


@dataclass(kw_only=True)
class SetConstraint(Constraint):
    # bag of...
    where: ExpressionType | None = field(default=None)
    constraint: ExpressionType | None = field(default=None)
