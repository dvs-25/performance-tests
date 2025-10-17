from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan, SeedOperationsPlan


class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    @property
    def plan(self) -> SeedsPlan:
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,
                credit_card_accounts=SeedAccountsPlan(
                    count=1,
                    top_up_operations=SeedOperationsPlan(count=1),
                    purchase_operations=SeedOperationsPlan(count=5),
                    cash_withdrawal_operations=SeedOperationsPlan(count=1),
                )
            )
        )

    @property
    def scenario(self) -> str:
        return "existing_user_get_operations"


if __name__ == '__main__':
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()
